from azure.iot.device import IoTHubDeviceClient
import time
from sensors import default

class Device():
    
    def __init__(self, device_connection_string,sensor_name="default",device_type=default, interval_s=30):
        self.client = IoTHubDeviceClient.create_from_connection_string(device_connection_string) 
        self.interval_s = interval_s
        self.sensor = device_type
        self.sensor_name=sensor_name
        self.stop_requested = False

    def set_interval(self, interval_s):
        self.interval_s = interval_s 
    
    def start(self):
        print(f"Starting device {self.sensor_name}")
        try:
            while not self.stop_requested:
                payload = self.sensor.generate_telemetry()
                print(f"\nTelemetry from {self.sensor_name}:\n======================\n{payload}\n======================\n")
                self.client.send_message(payload)
                time.sleep(self.interval_s)
        except Exception as e:
            print(f"Error while sending message in {self.sensor_name}: {e}")

    def stop(self):
        self.stop_requested = True