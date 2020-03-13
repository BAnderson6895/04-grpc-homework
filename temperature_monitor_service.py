from concurrent import futures
import grpc
import temperature_monitor_pb2
import temperature_monitor_pb2_grpc
import argparse
import psutil
import time

class TemperatureMonitor(temperature_monitor_pb2_grpc.TemperatureMonitorServicer):
    temp = []

    def CurrentTemperature(self, request, context):
        if not hasattr(psutil, 'sensors_temperatures'):
            return 40.0
        cur_temp = psutil.sensor_temperatures()['bcm2835_thermal'][0].current
        self.temp.append(cur_temp)
        return temperature_monitor_pb2_grpc.CurrentTemperature(celsius=cur_temp)
        

    def Temperatures(self, request, context):
        while context.is_active():
            time.sleep(1)
            yield CurrentTemperature()

    def MinMaxTemperature(self, request, context):
        if len(temp) == 0:
            return temperature_monitor_pb2_grpc.MinMaxTemperature(min=40.0, max=40.0)
        min_temp = min(self.temp)
        max_temp = max(self.temp)
        return temperature_monitor_pb2_grpc.MinMaxTemperature(min=min_temp, max=max_temp)
            

    def StressTest(self, request, context):
        cur_time = round(time.monotonic())
        stop_time = round(cur_time + request.seconds)
        number = 0
        while cur_time != stop_time:
            number = number + 1


def main():
    #TODO: Argparse port info or no info
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_monitor_pb2_grpc.add_TemperatureMonitorServicer_to_server(TemperatureMonitor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()
