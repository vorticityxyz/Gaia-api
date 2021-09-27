# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dispatch_pb2 as dispatch__pb2


class DispatchServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DispatchServerAddressRequest = channel.unary_unary(
                '/DispatchServer/DispatchServerAddressRequest',
                request_serializer=dispatch__pb2.AddressRequest.SerializeToString,
                response_deserializer=dispatch__pb2.AddressReply.FromString,
                )


class DispatchServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DispatchServerAddressRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DispatchServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DispatchServerAddressRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.DispatchServerAddressRequest,
                    request_deserializer=dispatch__pb2.AddressRequest.FromString,
                    response_serializer=dispatch__pb2.AddressReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DispatchServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DispatchServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DispatchServerAddressRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DispatchServer/DispatchServerAddressRequest',
            dispatch__pb2.AddressRequest.SerializeToString,
            dispatch__pb2.AddressReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
