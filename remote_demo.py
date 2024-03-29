# Description:
# 
# This example shows how to use Vorticity gaia remote operators to get
# shot records in batch model from a large survey.
# 
# remoteUpload: Uploads the entire model on to the remote server. This 
# allows other seismic operators to refer to the model when calling the 
# function as apposed to uploading it each time
#
# remoteDelete: Deletes un uploaded model from the remote server
# 
# rbf28pml: Runs the forward model in batch mode. This function will download
# shot records as they become available without waiting for the completion of 
# full project
#
# Input parameters for the operator is generated by the 
# function generate_test_data() and is as follows:
#
# model - 3D numpy array representing the ful velocity model
# shobox - Defines the dimensions of the shotbox to run the forward operator
# sweep - Defines starting location, ending location and step size of the sweep 
# shot - 1D numpy array representing the shot profile spanning the all timesteps
# shotxyz - Cartesian coordinates of the shot location
# recxxyyz - Cartesian coordinates of the receiver locations
# deltas - dx, dy, dz and dt for the simulation
# pml - width and amplitude of the PML layer
# destination - destination folder where you want the operator to save the shot records
#
# Output: simulated shot record in the form of a 3d numpy array of the format
# shot_record[timestep, x_position, y_position]
# 
# (C) Vorticity Inc. Mountain View, CA 2021
# Licence: MIT

import numpy as np
from pathlib import Path
import gaia

# Generate shot profile
def generate_ricker(nt, freq, dt):
    max_amplitude = 1
    npt = nt * dt
    t = np.arange(-float(npt)/2, float(npt)/2, dt)
    # generate the short waveform
    rick1 = max_amplitude * (1 - t * t * freq**2 * np.pi**2) * np.exp(-t**2 * np.pi**2 * freq**2)
    # Overlay the short waveform over the full length of timesteps
    rick = np.zeros(nt, dtype=np.float32)
    rick[0: nt - (round(nt/2) - round(1/freq/dt) + 1)] = rick1[round(nt/2) - round(1/freq/dt) + 1: nt];
    return rick

def generate_remote_data(model_file):
    # Full earth model dimensions
    nx = 1001 
    ny = 501
    nz = 501 

    # Dimensions of the shotbox for each shot record
    snx = 501 
    sny = 501 
    snz = 501 

    ghost = 4       # ghost points in a 8 spacial stencil

    # Spacial discretization
    dx = 2.5
    dy = dx
    dz = dx

    # temporal discretization
    dt = 0.0004

    # number of timesteps
    nt = 2500

    # Shot parameters (relative to shotbox)
    F = 30
    xs = round(snx/2)
    ys = round(sny/2)
    zs = ghost

    # Absorbing boundaries
    pmlw = 50
    pmla = 100

    # Receiver parameters (relative to shotbox)
    xt1 = pmlw + ghost
    xt2 = (snx - pmlw - ghost - 1)
    yt1 = round(sny/2)
    yt2 = round(sny/2)
    zt = ghost

    # x sweep parameters (relative to global model)
    xsrt = 0         # starting x position of shot box
    xend = 2         # ending x position of shot box
    xstp = 1         # step length in x direction

    ysrt = 0         # starting y position of shot box
    yend = 0         # ending y position of shot box
    ystp = 0         # step length in y direction

    # Earth model setup
    c1 = 1500
    c2 = 2500

    # Generate earth model
    model = np.full((nx, ny, nz), c1, dtype=np.float32)   # smooth model
    model[:, :, 151:] = c2                                                  # insert step

    shotbox = np.array([snx, sny, snz], dtype=np.int32)
    sweep = np.array([xsrt, xend, xstp, ysrt, yend, ystp], dtype=np.int32)
    shot = generate_ricker(nt, F, dt)
    shotxyz = np.array([xs, ys, zs], dtype=np.int32)
    recxxyyz = np.array([xt1, xt2, yt1, yt2, zt], dtype=np.int32)
    deltas = np.array([dx, dy, dz, dt], dtype=np.float32)
    pml = np.array([pmlw, pmla], dtype=np.int32)

    np.save(model_file, model)
    return shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml

if __name__ == '__main__':
    
    model_file = 'data/_rupload.npy'
    remote_file = 'rtest01.npy'
    destination = "results/"

    shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml = generate_remote_data(model_file)

    # Upload the earth model to remote server
    gaia.remoteUpload(model_file, remote_file)

    # Run batch forward operator on remote earth model. Shots will be saved in the destination folder
    gaia.rbf28pml(remote_file, shotbox, sweep, shot, shotxyz, recxxyyz, deltas, pml, destination)

    # Deletes the earth model from the remote server
    gaia.remoteDelete(remote_file)