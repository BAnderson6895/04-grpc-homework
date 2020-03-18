import grpc

import temperature_monitor_pb2
import temperature_monitor_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = temperature_monitor_pb2_grpc.TemperatureMonitorStub(channel)
    response = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
    print("Client received: " + str(response.celsius))
    response2 = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
    print("Client received: " + str(response.celsius))
    response3 = stub.MinMaxTemperature(temperature_monitor_pb2.Empty())
    print("Client received: " + str(response.min))
    print("Client received: " + str(response.max))


if __name__ == '__main__':
    main()
