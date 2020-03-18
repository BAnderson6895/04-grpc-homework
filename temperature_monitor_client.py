import grpc

import temperature_monitor_pb2
import temperature_monitor_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = temperature_monitor_pb2_grpc.ProductInfoStub(channel)
        response = stub.CurrentTemperature(temperature_monitor_pb2.Empty())
        print("Client received: " + response.message)


if __name__ == '__main__':
    main()
