import grpc

import temperature_monitor_pb2
import temperature_monitor_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = temperature_monitor_pb2_grpc.TemperatureMonitorStub(channel)
    response = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
    response2 = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
    response3 = stub.MinMaxTemperature(temperature_monitor_pb2.Empty())
    print("Client received: " + str(response.celsius))
    print("Client received: " + str(response2.celsius))
    print("Client received min: " + str(response3.min) + " max: " + str(response3.max))


if __name__ == '__main__':
    main()
