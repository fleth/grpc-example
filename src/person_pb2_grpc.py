# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import person_pb2 as person__pb2


class InfomationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/tutorial.Infomation/Get',
        request_serializer=person__pb2.Params.SerializeToString,
        response_deserializer=person__pb2.Person.FromString,
        )


class InfomationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InfomationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=person__pb2.Params.FromString,
          response_serializer=person__pb2.Person.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tutorial.Infomation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
