from concurrent import futures
import grpc
import temperature_monitor_pb2
import temperature_monitor_pb2_grpc
import argparse
import time
import psutil


class TemperatureMonitor(temperature_monitor_pb2_grpc.TemperatureMonitorServicer):
    temperatures = []

    def CurrentTemperature(self, request, context):
        """
        CurrentTemperature function will check to see what the current temperature of the Raspberry Pi is.
        If psutil is not present, it will return a default value of 40 degrees.
        When the temperature is checked, it will add the temperature received to a temperature array.
        The method returns a Temperature object.
        """
        if not hasattr(psutil, 'sensors_temperatures'):
            return temperature_monitor_pb2_grpc.CurrentTemperature(celsius=40.0)
        cur_temp = psutil.sensors_temperatures()['bcm2835_thermal'][0].current
        self.temperatures.append(cur_temp)
        return temperature_monitor_pb2.Temperature(celsius=cur_temp)
        

    def Temperatures(self, request, context):
        """
        The Temperatures function will yield a continuous stream of temperature objects until
        the user cancels the stream.
        """
        while context.is_active():
            time.sleep(1)
            yield Temperature(self, request, context)


    def MinMaxTemperature(self, request, context):
        """
        MinMaxTemperature will check all the temperatures stored in the temperatures array that
        were received by the CurrentTemperature method and return the minimum and maximum
        temperatures in a minmax object.
        """
        if len(temperatures) == 0:
            return temperature_monitor_pb2.MinMaxTemperature(min=40.0, max=40.0)
        min_temp = min(self.temperatures)
        max_temp = max(self.temperatures)
        return temperature_monitor_pb2.MinMax(min=min_temp, max=max_temp)
            

    def StressTest(self, request, context):
        """
        StressTest will take a number parameter for how many seconds to loop for
        and keep adding one to an integer until the specified number of seconds
        of time has passed. The times will not match up exactly given that time.monotonic()
        gives a time to seven decimal places, so the round() method is used to ensure
        that the variables of cur_time and stop_time will match up and break the loop.
        """
        cur_time = round(time.monotonic())
        stop_time = round(cur_time + request.seconds)
        number = 0
        while cur_time != stop_time:
            number = number + 1
            cur_time = round(time.monotonic())
            

def main():
    parser = argparse.ArgumentParser(description='Run temperature monitor gRPC server.')
    parser.add_argument('--port', type=int, help='port number to use', default=50051)
    args = parser.parse_args()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_monitor_pb2_grpc.add_TemperatureMonitorServicer_to_server(TemperatureMonitor(), server)
    server.add_insecure_port('[::]:' + str(args.port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()
