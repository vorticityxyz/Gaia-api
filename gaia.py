# Description:
#
# WARNING!!! This file is a critical component of Vorticity Gaia API for seismic imaging
# PLEASE DO NOT MODIFY
#
# (C) Vorticity Inc. Mountain View, CA 2021
# Licence: MIT

import numpy as np
import grpc
import time
import os
import sys
import gaia_pb2
import gaia_pb2_grpc
import dispatch_pb2
import dispatch_pb2_grpc
import validate

import tokens
import codes

CHUNK_SIZE = 1024 * 1024  # 1MB

IN_FILE = "_gaia_input.npz"
EL_IN_FILE = "_egaia_input.npz"
RTM_FILE = "_gaia_rtm.npz"
EL_RTM_FILE = "_gaia_ertm.npz"
BF_FILE = "_gaia_block.npz"
OUT_FILE = "_shot_record.npy"
EL_OUT_FILE = "_eshot_record.npz"
UPDATE_FILE = "_rtm_update.npy"
EL_UPDATE_FILE = "_ertm_update.npz"
SANITY_FILE = "_parameters.npy"
EL_SANITY_FILE = "_eparameters.npy"
BF_SANILTY_FILE = "_bfparameters.npy"
RBF_SETUP_FILE = '_rbf_setup.npz'

DISPATCH_SERVER = 'vorticity.cloud:443'

def get_file_chunks(filename):
    with open(filename, 'rb') as f:
        size = 0
        while True:
            piece = f.read(CHUNK_SIZE);
            size += sys.getsizeof(piece)
            if len(piece) == 0:
                print()
                return
            yield gaia_pb2.Chunk(buffer=piece)
            sys.stdout.write('\r')
            sys.stdout.write('Uploading %.1f MB' % (size/CHUNK_SIZE,))
            sys.stdout.flush()

def get_file_chunks_nv(filename):
    with open(filename, 'rb') as f:
        size = 0
        while True:
            piece = f.read(CHUNK_SIZE);
            size += sys.getsizeof(piece)
            if len(piece) == 0:
                return
            yield gaia_pb2.Chunk(buffer=piece)

def save_chunks_to_file(chunks, filename):
    size = 0
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.buffer)
            size += sys.getsizeof(chunk.buffer)
            sys.stdout.write('\r')
            sys.stdout.write('Downloading %.1f MB' % (size/CHUNK_SIZE,))
            sys.stdout.flush()
        
        print()

def show_progress(responses):
    final_progress_value = 0.0
    for response in responses:
        sys.stdout.write('\r')
        sys.stdout.write('%.2f%% complete' % (response.progress * 100,))
        sys.stdout.flush()
        final_progress_value = response.progress
    print()
    return final_progress_value


class DispatchClient:
    def __init__(self, address):
        with open('server.crt', 'rb') as f:
            creds = grpc.ssl_channel_credentials(f.read())
        channel = grpc.secure_channel(address, creds, 
                                      options = (('grpc.ssl_target_name_override', 'localhost'), 
                                                 ('grpc.default_authority', 'localhost')),
                                      compression=grpc.Compression.Gzip)
        self.stub = dispatch_pb2_grpc.DispatchServerStub(channel)

    def DispatchServerAddressRequest(self, token):
        request = dispatch_pb2.AddressRequest()
        request.token = token
        response = self.stub.DispatchServerAddressRequest(request)

        return response

class GaiaClient:
    def __init__(self, token):
        dispatch_client = DispatchClient(DISPATCH_SERVER)
        response = dispatch_client.DispatchServerAddressRequest(token)
        if (response.status == codes.SUCCESS):
            address = response.address
            with open('server.crt', 'rb') as f:
                creds = grpc.ssl_channel_credentials(f.read())
            channel = grpc.secure_channel(address, creds,
                                          options = (('grpc.ssl_target_name_override', 'localhost'), 
                                                     ('grpc.default_authority', 'localhost')),
                                          compression=grpc.Compression.Gzip)
            self.stub = gaia_pb2_grpc.GaiaServerStub(channel)
        else:
            raise Exception("We could not verify this account. Please contact Vorticity.")

    def StatusCheck(self, token):
        request = gaia_pb2.StatusRequest()
        request.token = token
        response = self.stub.StatusCheck(request)
        return response.status

    def SanityCheck(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.SanityCheck(chunks_generator)
        return response.status

    def rtmSanityCheck(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.rtmSanityCheck(chunks_generator)
        return response.status

    def eForwardSanityCheck(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.eForwardSanityCheck(chunks_generator)
        return response.status
    
    def eRTMSanityCheck(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.eRTMSanityCheck(chunks_generator)
        return response.status

    def Upload(self, file_name):
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.Upload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def rtmUpload(self, file_name):
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.rtmUpload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def eForwardUpload(self, file_name):
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.eForwardUpload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def eRTMUpload(self, file_name):
        print("Uploading...")
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.eRTMUpload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def Execute(self, sent_token):
        print("Forward processing.")
        start = time.time()
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        responses = self.stub.Execute(request)
        final_progress_value = show_progress(responses)
        end = time.time()
        process_time = end - start
        print("Processing time:", "{:.2f}".format(process_time), 's')
        return final_progress_value

    def rtmExecute(self, sent_token):
        print("RTM processing.")
        start = time.time()
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        responses = self.stub.rtmExecute(request)
        final_progress_value = show_progress(responses)
        end = time.time()
        process_time = end - start
        print("Processing time:", "{:.2f}".format(process_time), 's')
        return final_progress_value

    def eForwardExecute(self, sent_token):
        print("Elastic forward processing.")
        start = time.time()
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        responses = self.stub.eForwardExecute(request)
        final_progress_value = show_progress(responses)
        end = time.time()
        process_time = end - start
        print("Processing time:", "{:.2f}".format(process_time), 's')
        return final_progress_value

    def eRTMExecute(self, sent_token):
        print("Elastic RTM processing.")        
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        responses = self.stub.eRTMExecute(request)
        final_progress_value = show_progress(responses)
        return final_progress_value

    def Download(self, sent_token, out_file_name):
        print("Downloading results")
        start = time.time()
        request = gaia_pb2.DownloadRequest()
        request.token = sent_token
        response = self.stub.Download(request)
        save_chunks_to_file(response, out_file_name)
        end = time.time()
        download_time = end - start
        print("Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_file_name)/download_time/1024/1024), 'MB/s' )

    def rtmDownload(self, sent_token, out_file_name):
        print("Downloading results")
        start = time.time()
        request = gaia_pb2.DownloadRequest()
        request.token = sent_token
        response = self.stub.rtmDownload(request)
        save_chunks_to_file(response, out_file_name)
        end = time.time()
        download_time = end - start
        print("Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_file_name)/download_time/1024/1024), 'MB/s' )

    def eForwardDownload(self, sent_token, out_file_name):
        print("Downloading results")
        start = time.time()
        request = gaia_pb2.DownloadRequest()
        request.token = sent_token
        response = self.stub.eForwardDownload(request)
        save_chunks_to_file(response, out_file_name)
        end = time.time()
        download_time = end - start
        print("Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_file_name)/download_time/1024/1024), 'MB/s' )

    def eRTMDownload(self, sent_token, out_file_name):
        print("downloading...")
        start = time.time()
        request = gaia_pb2.DownloadRequest()
        request.token = sent_token
        response = self.stub.eRTMDownload(request)
        save_chunks_to_file(response, out_file_name)
        end = time.time()
        download_time = end - start
        print("Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_file_name)/download_time/1024/1024), 'MB/s' )

    def CleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.CleanUp(request)
        return response.status

    def rtmCleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.rtmCleanUp(request)
        return response.status

    def eForwardCleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.eForwardCleanUp(request)
        return response.status

    def eRTMCleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.eRTMCleanUp(request)
        return response.status

    def BatchForwardSanityCheck(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.BatchForwardSanityCheck(chunks_generator)
        return response.status

    def BatchForwardStatus(self, token, filename):
        request = gaia_pb2.BatchStatusRequest()
        request.token = token
        request.filename = filename
        response = self.stub.BatchForwardStatus(request)
        return response

    def BatchForwardUpload(self, file_name):
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.BatchForwardUpload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def BatchForwardInitExec(self, sent_token):
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        response = self.stub.BatchForwardInitExec(request)
        return response.status

    def BatchForwardDownload(self, sent_token, sent_filename, out_filename):
        #print("Downloading", sent_filename)
        start = time.time()
        request = gaia_pb2.BatchDownloadRequest()
        request.token = sent_token
        request.filename = sent_filename
        responses = self.stub.BatchForwardDownload(request)
        size = 0
        with open(out_filename, 'wb') as f:
            for response in responses:
                f.write(response.buffer)
                size += sys.getsizeof(response.buffer)
                sys.stdout.write('\r')
                sys.stdout.write(out_filename + ' - %.1f MB' % (size/CHUNK_SIZE,))
                sys.stdout.flush()

        #print()
        end = time.time()
        download_time = end - start
        print(" Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_filename)/download_time/1024/1024), 'MB/s' )

    def BatchForwardCleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.BatchForwardCleanUp(request)
        return response.status

    def rUploadSanityCheck(self, sent_token, filename, filesize):
        request = gaia_pb2.RemoteUploadSanityRequest()
        request.token = sent_token
        request.filename = filename
        request.filesize = filesize
        response = self.stub.rUploadSanityCheck(request)
        return response.status

    def rUpload(self, file_name):
        start = time.time()
        chunks_generator = get_file_chunks(file_name)
        response = self.stub.rUpload(chunks_generator)
        end = time.time()
        upload_time = end - start
        print("Upload time:", "{:.2f}".format(upload_time), 's', 
                    "speed:", "{:.2f}".format(os.path.getsize(file_name)/upload_time/1024/1024), 'MB/s')
        return response.length

    def rForwardUpload(self, file_name):
        chunks_generator = get_file_chunks_nv(file_name)
        response = self.stub.rForwardUpload(chunks_generator)
        return response

    def rForwardInitExec(self, sent_token):
        request = gaia_pb2.ExecuteRequest()
        request.token = sent_token
        response = self.stub.rForwardInitExec(request)
        return response.status

    def rForwardStatus(self, token, filename):
        request = gaia_pb2.BatchStatusRequest()
        request.token = token
        request.filename = filename
        response = self.stub.rForwardStatus(request)
        return response

    def rForwardDownload(self, sent_token, sent_filename, out_filename):
        start = time.time()
        request = gaia_pb2.BatchDownloadRequest()
        request.token = sent_token
        request.filename = sent_filename
        responses = self.stub.rForwardDownload(request)
        size = 0
        with open(out_filename, 'wb') as f:
            for response in responses:
                f.write(response.buffer)
                size += sys.getsizeof(response.buffer)
                sys.stdout.write('\r')
                sys.stdout.write(out_filename + ' - %.1f MB' % (size/CHUNK_SIZE,))
                sys.stdout.flush()

        #print()
        end = time.time()
        download_time = end - start
        print(" Download time:", "{:.2f}".format(download_time), 's',
                      "speed:", "{:.2f}".format(os.path.getsize(out_filename)/download_time/1024/1024), 'MB/s' )

    def rForwardCleanUp(self, sent_token):
        request = gaia_pb2.CleanUpRequest()
        request.token = sent_token
        response = self.stub.rForwardCleanUp(request)
        return response.status

    def rDelete(self, sent_token, filename):
        request = gaia_pb2.DeleteRequest()
        request.token = sent_token
        request.filename = filename
        response = self.stub.rDelete(request)
        return response.status

    def Reset(self, sent_token):
        request = gaia_pb2.ResetRequest()
        request.token = sent_token
        response = self.stub.Reset(request)
        return response.status

def reset_server():
    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # get the token for identification to server
    token = tokens.USER_TOKEN
    status = client.Reset(token)
    if (status == codes.SUCCESS):
        print("Server reset successful!")
    else:
        print("Error resetting server. Contact Vorticity.")

# Forward model operator
def f28(model, shot, shotxyz, recxxyyz, deltas):

    # temporal accuracy 2, spacial accuracy 8, no abc
    act = 2 
    acs = 8
    abc = 0
    cnum = 1        # num accelerator cards

    # no pml
    pmlw = 0
    pmla = 0

    # Validate that user input is usable
    validate.model(model)
    validate.shot(shot)
    validate.shotxyz(model, shotxyz)
    validate.recxxyyz(model, recxxyyz)
    validate.deltas(deltas)


    sanity_data = np.array([model.shape[0], model.shape[1], model.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            act, abc, cnum], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           act, acs, abc, pmlw, pmla, cnum], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")

    # Save data to disk for transfer
    np.savez(IN_FILE, model=np.square(model), shot=shot, config_int=config_int, config_float=config_float)
    np.save(SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.SanityCheck(SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, receiver size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.Upload(IN_FILE)
        if (file_length != os.path.getsize(IN_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.EXEC_READY):
        final_progress_value = client.Execute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download shot_record
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.Download(token, OUT_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.") 

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.CleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")

    # return data to user
    shot_record = np.load(OUT_FILE)
    os.remove(IN_FILE)
    os.remove(OUT_FILE)
    os.remove(SANITY_FILE)

    return shot_record

# Forward model operator with pml
def f28pml(model, shot, shotxyz, recxxyyz, deltas, pml):

    # temporal accuracy 2, spacial accuracy 8, pml
    act = 2 
    acs = 8
    abc = 1
    cnum = 1       # num accelerator cards

    # Validate that user input is usable
    validate.model(model)
    validate.shot(shot)
    validate.shotxyz(model, shotxyz)
    validate.recxxyyz(model, recxxyyz)
    validate.deltas(deltas)
    validate.pml(model, pml)

    sanity_data = np.array([model.shape[0], model.shape[1], model.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            act, abc, cnum], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           act, acs, abc,
                           pml[0], pml[1],    # no pml
                           cnum], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")

    # Save data to disk for transfer
    np.savez(IN_FILE, model=np.square(model), shot=shot, config_int=config_int, config_float=config_float)
    np.save(SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.SanityCheck(SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, receiver size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.Upload(IN_FILE)
        if (file_length != os.path.getsize(IN_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.EXEC_READY):
        final_progress_value = client.Execute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download shot_record
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.Download(token, OUT_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.") 

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.CleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")

    # return data to user
    shot_record = np.load(OUT_FILE)
    os.remove(IN_FILE)
    os.remove(OUT_FILE)
    os.remove(SANITY_FILE)

    return shot_record

# Multi accelerator card forward model operator
def mf28pml(model, shot, shotxyz, recxxyyz, deltas, pml):

    # temporal accuracy 2, spacial accuracy 8, pml
    act = 2 
    acs = 8
    abc = 1
    cnum = 2       # num accelerator cards

    # Validate that user input is usable
    validate.multicard_model(model, cnum)
    validate.shot(shot)
    validate.shotxyz(model, shotxyz)
    validate.recxxyyz(model, recxxyyz)
    validate.deltas(deltas)
    validate.pml(model, pml)

    sanity_data = np.array([model.shape[0], model.shape[1], model.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            act, abc, cnum], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           act, acs, abc,
                           pml[0], pml[1],    # no pml
                           cnum], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")

    # Save data to disk for transfer
    np.savez(IN_FILE, model=np.square(model), shot=shot, config_int=config_int, config_float=config_float)
    np.save(SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.SanityCheck(SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, receiver size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.Upload(IN_FILE)
        if (file_length != os.path.getsize(IN_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.EXEC_READY):
        final_progress_value = client.Execute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download shot_record
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.Download(token, OUT_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.") 

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.CleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")

    # return data to user
    shot_record = np.load(OUT_FILE)
    os.remove(IN_FILE)
    os.remove(OUT_FILE)
    os.remove(SANITY_FILE)

    return shot_record

# Acoustic RTM operator
def rtm28pml(model, shot, traces, shotxyz, recxxyyz, deltas, pml):
    
    # temporal accuracy 2, spacial accuracy 8, with pml
    act = 2 
    acs = 8
    abc = 1

    # Validate that user input is usable
    validate.model(model)
    validate.shot(shot)
    validate.traces(traces, shot, model)
    validate.shotxyz(model, shotxyz)
    validate.recxxyyz(model, recxxyyz)
    validate.deltas(deltas)
    validate.pml(model, pml)

    sanity_data = np.array([model.shape[0], model.shape[1], model.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            act, abc], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           act, acs, abc,
                           pml[0], pml[1],    # no pml
                           ], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")

    # Save data to disk for transfer
    np.savez(RTM_FILE, model=np.square(model), shot=shot, traces=traces, config_int=config_int, config_float=config_float)
    np.save(SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.rtmSanityCheck(SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, trace size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.rtmUpload(RTM_FILE)
        if (file_length != os.path.getsize(RTM_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.RTM_READY):
        final_progress_value = client.rtmExecute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download shot_record
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.rtmDownload(token, UPDATE_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.") 

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.rtmCleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")

    # return data to user
    update = np.load(UPDATE_FILE)
    os.remove(RTM_FILE)
    os.remove(UPDATE_FILE)
    os.remove(SANITY_FILE)

    return update

# Elastic forward model operator
def ef18abc(vp, vs, rho, shot, shotxyz, recxxyyz, deltas, abc):

    # temporal accuracy 2, spacial accuracy 8, with sponge
    temportal_ac = 1
    spacial_ac = 8
    abc_type = 2

    # Validate that user input is usable
    validate.emodel(vp, vs, rho)
    validate.shot(shot)
    validate.shotxyz(vp, shotxyz)
    validate.recxxyyz(vp, recxxyyz)
    validate.deltas(deltas)
    validate.abc(vp, abc)

    sanity_data = np.array([vp.shape[0], vp.shape[1], vp.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            temportal_ac, abc_type], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           temportal_ac, spacial_ac, abc_type,
                           abc[0], abc[1],
                           ], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")

    # Save data to disk for transfer
    np.savez(EL_IN_FILE, vp=np.square(vp), vs=np.square(vs), rho=rho, shot=shot, config_int=config_int, config_float=config_float)
    np.save(EL_SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.eForwardSanityCheck(EL_SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources with the current Vorticity instance.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.eForwardUpload(EL_IN_FILE)
        if (file_length != os.path.getsize(EL_IN_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.EXEC_READY):
        final_progress_value = client.eForwardExecute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download vx, vy and vz records
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.eForwardDownload(token, EL_OUT_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.") 

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.eForwardCleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")
            
    with np.load(EL_OUT_FILE) as results:
        vx_traces = results['vx']
        vy_traces = results['vy']
        vz_traces = results['vz']

    os.remove(EL_IN_FILE)
    os.remove(EL_OUT_FILE)
    os.remove(EL_SANITY_FILE)

    return vx_traces, vy_traces, vz_traces

# Elastic RTM operator
def ertm18abc(vp, vs, rho, shot, vx, vy, vz, shotxyz, recxxyyz, deltas, abc):
    # temporal accuracy 2, spacial accuracy 8, with sponge
    temportal_ac = 1
    spacial_ac = 8
    abc_type = 2

    # Validate that user input is usable
    validate.emodel(vp, vs, rho)
    validate.shot(shot)
    validate.traces(vx, shot, vp)
    validate.traces(vy, shot, vp)
    validate.traces(vz, shot, vp)
    validate.shotxyz(vp, shotxyz)
    validate.recxxyyz(vp, recxxyyz)
    validate.deltas(deltas)
    validate.abc(vp, abc)

    sanity_data = np.array([vp.shape[0], vp.shape[1], vp.shape[2], shot.shape[0],
                            recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3],
                            temportal_ac, abc_type], dtype=np.int32)

    config_int = np.array([shotxyz[0], shotxyz[1], shotxyz[2],
                           recxxyyz[0], recxxyyz[1], recxxyyz[2], recxxyyz[3], recxxyyz[4],
                           temportal_ac, spacial_ac, abc_type,
                           abc[0], abc[1],
                           ], dtype=np.int32)
    config_float = deltas

    print("Starting gaia process.")
    np.savez(EL_RTM_FILE, vp=np.square(vp), vs=np.square(vs), rho=rho, shot=shot, vx=vx, vy=vy, vz=vz, config_int=config_int, config_float=config_float)
    np.save(EL_SANITY_FILE, sanity_data)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.eRTMSanityCheck(EL_SANITY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, trace size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.eRTMUpload(EL_RTM_FILE)
        if (file_length != os.path.getsize(EL_RTM_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.StatusCheck(token)
    if (status == codes.RTM_READY):
        final_progress_value = client.eRTMExecute(token)
        if (final_progress_value != 1.0):
            raise Exception("Something went wrong. Try again in a bit and if problem persists, contact Vorticity.")
    else:
        raise Exception("Server not ready. Try again in a few minites.")

    # Download shot_record
    status = client.StatusCheck(token)
    if (status == codes.DOWNLOAD_READY):
        client.eRTMDownload(token, EL_UPDATE_FILE)
    else:
        raise Exception("Server not ready. Try again in a few minites. If the problem persists, contact Vorticity.")

    # Clean up remote server
    status = client.StatusCheck(token)
    if (status == codes.CLEANUP_READY):
        status = client.eRTMCleanUp(token)
        if (status == codes.SUCCESS):
            print("Process complete!")
        else:
            print("Process did not complete as intended. Contact Vorticity.")

    # Load update data
    with np.load(EL_UPDATE_FILE) as data:
        dvp = data['dvp']
        dvs = data['dvs']

    # remove all temp files
    os.remove(EL_RTM_FILE)
    os.remove(EL_UPDATE_FILE)
    os.remove(EL_SANITY_FILE)

    return dvp, dvs

# Batch forward model operator
def batchf28pml(block, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml, destination):
    # simulation parameters
    act = 2
    acs = 8       # spacial accuracy
    # absorbing boundary conditions
    # 0 - none, 1 - pml
    abc = 1
    cnum = 2     # number of accelerator cards to use

    # Validate that user input is usable
    validate.block(block)
    validate.shotbox(block, shotbox)
    validate.sweep(block, shotbox, sweep)
    validate.shot(shot)

    shotbox_nx = shotbox[0]
    shotbox_ny = shotbox[1]
    shotbox_nz = shotbox[2]

    ghost_model = np.empty((shotbox_nx, shotbox_ny, shotbox_nz))

    validate.shotxyz(ghost_model, shotxyz)
    validate.recxxyyz(ghost_model, recxxyyz)
    validate.deltas(deltas)
    validate.pml(ghost_model, pml)

    nt = shot.shape[0]
    xt1 = recxxyyz[0]
    xt2 = recxxyyz[1]
    yt1 = recxxyyz[2]
    yt2 = recxxyyz[3]
    zt = recxxyyz[4]

    x_start = sweep[0]
    x_end = sweep[1]
    x_step = sweep[2]
    y_start = sweep[3]
    y_end = sweep[4]
    y_step = sweep[5]

    sim = np.array([act, acs, abc, cnum], dtype=np.int32)
    sanity_data = np.array([shotbox_nx, shotbox_ny, shotbox_nz, nt, xt1, xt2, yt1, yt2, act, abc, cnum])

    print("Starting gaia process.")
    np.save(BF_SANILTY_FILE, sanity_data)
    np.savez(BF_FILE, model=block, shotbox=shotbox, sweep=sweep, shot=shot, shotxyz=shotxyz, recxxyyz=recxxyyz, deltas=deltas, sim=sim, pml=pml)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Do a quick sanity check to ensure simulation parameters are within server bounds
    status = client.BatchForwardSanityCheck(BF_SANILTY_FILE)
    if (status == codes.ERROR):
        raise Exception("This simulation will take too many resources. Try again with a lower resolution, trace size and/or timesteps.")

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        file_length = client.BatchForwardUpload(BF_FILE)
        if (file_length != os.path.getsize(BF_FILE)):
            raise Exception("Something went wrong with data upload to server. Try again in a bit or if problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")
    
    # Now instigate execution
    status = client.BatchForwardInitExec(token)
    if (status == codes.ERROR):
        raise Exception("Something went wrong when instigating batch execution. Try again after resetting the server or if problem persists, contact Vorticity.")

    y_offset = y_start
    x_offset = x_start

    while (y_offset <= y_end):
        while (x_offset <= x_end):
            filename = "shot-" + str(y_offset) + "-" + str(x_offset) + ".npy"
            drop_point = destination + filename

            while(True):
                response = client.BatchForwardStatus(token, filename)
                sys.stdout.write('\r')
                sys.stdout.write('Processing shot %d of %d | %.2f%%' % (response.shot, response.total, response.progress * 100,))
                sys.stdout.flush()
                if (response.progress == 1.0):
                    break
                #time.sleep(0.02)
            
            print()
            while(True):
                response = client.BatchForwardStatus(token, filename)
                if (response.fileExists == True):
                    break
                #time.sleep(0.02)

            client.BatchForwardDownload(token, filename, drop_point)
            
            if (x_step == 0):
                break
            x_offset += x_step
        
        if (y_step == 0):
            break
        x_offset = x_start
        y_offset += y_step

    status = client.BatchForwardCleanUp(token)
    if (status == codes.SUCCESS):
        print("Process complete!")
    else:
        print("Process did not complete as intended. Contact Vorticity.")

    # remove all temp files
    os.remove(BF_FILE)
    os.remove(BF_SANILTY_FILE)

# remote upload operator
def remoteUpload(local_filename, remote_filename):

    with open(local_filename, 'rb') as fobj:
        version = np.lib.format.read_magic(fobj)
        if version[0] == 1:
            shape, fortran_order, dtype = np.lib.format.read_array_header_1_0(fobj)
        else:
            shape, fortran_order, dtype = np.lib.format.read_array_header_2_0(fobj)

    # Validate that user input is usable
    validate.remote_model(shape, dtype)

    print("Starting gaia process.")

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    file_size = os.path.getsize(local_filename)
    sanity_status = client.rUploadSanityCheck(token, remote_filename, file_size)

    if (sanity_status == codes.ERROR):
        raise Exception("Unable to upload. Not enough free space on remote server.")

    response = client.rUpload(local_filename)

    if (response != file_size):
        raise Exception("Something went wrong with data upload to server. Try a gaia reset or if problem persists, contact Vorticity.")

    print("Process complete!")

# remote batch forward operator
def rbf28pml(modelfile, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml, destination):
    # simulation parameters
    act = 2
    acs = 8       # spacial accuracy
    # absorbing boundary conditions
    # 0 - none, 1 - pml
    abc = 1
    cnum = 2     # number of accelerator cards to use

    validate.shot(shot)
    snx = shotbox[0]
    sny = shotbox[1]
    snz = shotbox[2]

    ghost_model = np.empty((snx, sny, snz))

    validate.shotxyz(ghost_model, shotxyz)
    validate.recxxyyz(ghost_model, recxxyyz)
    validate.deltas(deltas)
    validate.pml(ghost_model, pml)

    xs = shotxyz[0]
    ys = shotxyz[1]
    zs = shotxyz[2]

    nt = shot.shape[0]
    xt1 = recxxyyz[0]
    xt2 = recxxyyz[1]
    yt1 = recxxyyz[2]
    yt2 = recxxyyz[3]
    zt = recxxyyz[4]

    xsrt = sweep[0]
    xend = sweep[1]
    xstp = sweep[2]
    ysrt = sweep[3]
    yend = sweep[4]
    ystp = sweep[5]

    sim = np.array([act, acs, abc, cnum], dtype=np.int32)

    print("Starting gaia process.")
    np.savez(RBF_SETUP_FILE, 
        modelfile=modelfile, shotbox=shotbox, sweep=sweep, shot=shot, shotxyz=shotxyz, recxxyyz=recxxyyz, deltas=deltas, sim=sim, pml=pml)

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    # Check if server is ready for upload and if so upload file
    status = client.StatusCheck(token)
    if (status == codes.UPLOAD_READY):
        response = client.rForwardUpload(RBF_SETUP_FILE)
        if (response.status != codes.SUCCESS):
            raise Exception("Simulation was rejected by the server. Possible incorrect setup.")

        if (response.length != os.path.getsize(RBF_SETUP_FILE)): 
            raise Exception("Error uploading simulation. Reset server and try again. If problem persists, contact Vorticity.")
    else:
        raise Exception("Server busy. Wait for the original task to complete.")

    # Now instigate execution
    status = client.rForwardInitExec(token)
    if (status == codes.ERROR):
        raise Exception("Something went wrong when instigating execution. Try again after resetting the server or if problem persists, contact Vorticity.")

    y_offset = ysrt
    x_offset = xsrt

    while (y_offset <= yend):
        while (x_offset <= xend):
            filename = "shot-" + str(x_offset + xs) + "-" + str(y_offset + ys) + ".npy"
            drop_point = destination + filename

            while(True):
                response = client.rForwardStatus(token, filename)
                if (response.fileExists == True):
                    break
                sys.stdout.write('\r')
                sys.stdout.write('Processing shot %d of %d | %.2f%%' % (response.shot, response.total, response.progress * 100,))
                sys.stdout.flush()
                if (response.progress == 1.0):
                    print()
                    break

            while(True):
                response = client.rForwardStatus(token, filename)
                if (response.fileExists == True):
                    break
                #time.sleep(0.02)

            client.rForwardDownload(token, filename, drop_point)

            if (xstp == 0):
                break
            x_offset += xstp
        
        if (ystp == 0):
            break
        x_offset = xsrt
        y_offset += ystp

    status = client.rForwardCleanUp(token)
    if (status == codes.SUCCESS):
        print("Process complete!")
    else:
        print("Process did not complete as intended. Contact Vorticity.")

    # remove all temp files
    os.remove(RBF_SETUP_FILE)

# remote delte operator
def remoteDelete(remote_filename):
    print("Starting gaia process.")

    # get the token for identification to server
    token = tokens.USER_TOKEN

    # Launch client
    client = GaiaClient(token)

    print("Deleting remote earth model.")
    status = client.rDelete(token, remote_filename)

    if (status == codes.SUCCESS):
        print("Process complete!")
    else:
        print("Process did not complete as intended. Contact Vorticity.")