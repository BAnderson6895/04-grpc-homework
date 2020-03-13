# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import temperature_monitor_pb2 as temperature__monitor__pb2


class TemperatureMonitorStub(object):
  """A service that allows you to monitor the temperature of the CPU 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CurrentTemperature = channel.unary_unary(
        '/TemperatureMonitor/CurrentTemperature',
        request_serializer=temperature__monitor__pb2.Empty.SerializeToString,
        response_deserializer=temperature__monitor__pb2.Temperature.FromString,
        )
    self.Temperatures = channel.unary_stream(
        '/TemperatureMonitor/Temperatures',
        request_serializer=temperature__monitor__pb2.Time.SerializeToString,
        response_deserializer=temperature__monitor__pb2.Temperature.FromString,
        )
    self.MinMaxTemperature = channel.unary_unary(
        '/TemperatureMonitor/MinMaxTemperature',
        request_serializer=temperature__monitor__pb2.Empty.SerializeToString,
        response_deserializer=temperature__monitor__pb2.MinMax.FromString,
        )
    self.StressTest = channel.unary_unary(
        '/TemperatureMonitor/StressTest',
        request_serializer=temperature__monitor__pb2.Time.SerializeToString,
        response_deserializer=temperature__monitor__pb2.Empty.FromString,
        )


class TemperatureMonitorServicer(object):
  """A service that allows you to monitor the temperature of the CPU 
  """

  def CurrentTemperature(self, request, context):
    """Gets the current CPU temperature 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Temperatures(self, request, context):
    """Gets the current CPU temperatures as a stream, with a delay between each response 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MinMaxTemperature(self, request, context):
    """Gets the minimum and maxium temperatures recorded 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StressTest(self, request, context):
    """Causes a stess test to run for the given duration 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TemperatureMonitorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CurrentTemperature': grpc.unary_unary_rpc_method_handler(
          servicer.CurrentTemperature,
          request_deserializer=temperature__monitor__pb2.Empty.FromString,
          response_serializer=temperature__monitor__pb2.Temperature.SerializeToString,
      ),
      'Temperatures': grpc.unary_stream_rpc_method_handler(
          servicer.Temperatures,
          request_deserializer=temperature__monitor__pb2.Time.FromString,
          response_serializer=temperature__monitor__pb2.Temperature.SerializeToString,
      ),
      'MinMaxTemperature': grpc.unary_unary_rpc_method_handler(
          servicer.MinMaxTemperature,
          request_deserializer=temperature__monitor__pb2.Empty.FromString,
          response_serializer=temperature__monitor__pb2.MinMax.SerializeToString,
      ),
      'StressTest': grpc.unary_unary_rpc_method_handler(
          servicer.StressTest,
          request_deserializer=temperature__monitor__pb2.Time.FromString,
          response_serializer=temperature__monitor__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TemperatureMonitor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
