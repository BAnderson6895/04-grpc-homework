import grpc

import temperature_monitor_pb2
import temperature_monitor_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = temperature_monitor_pb2_grpc.TemperatureMonitorStub(channel)
    response = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
    print("Client received: " + response.celsius)


if __name__ == '__main__':
    main()
