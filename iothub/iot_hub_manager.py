from azure.iot.hub import IoTHubRegistryManager
import uuid
import time
import sys
import json
from dotenv import dotenv_values
from cachetools import cached, LRUCache, TTLCache

class IotHubManager():
    
    def __init__(self) -> None:    
        self.iot_hub_connection_string=f"HostName={dotenv_values('.env')['HostName']};SharedAccessKeyName={dotenv_values('.env')['SharedAccessKeyName']};SharedAccessKey={dotenv_values('.env')['SharedAccessKey']}"
        self.registry_manager = IoTHubRegistryManager(self.iot_hub_connection_string)
        self.connection_pool = self.get_device_connection_strings()


    def get_device_connection_strings(self):
        
        device_connection_strings=[]
         # Try to read existing connection strings from the file
        try:
            with open("cached_connections.json", "r") as localCacheFile:
                device_connection_strings = json.load(localCacheFile)
            
             # If connections already exist, return values
            if device_connection_strings:
                return device_connection_strings

        except:
            with open("cached_connections.json","w") as localCacheFile:
                print("Cache file created")
       
            
            # If not, write into file and return the first instance
            devices = self.registry_manager.get_devices()
            for device in devices:
                twin = self.registry_manager.get_twin(device.device_id)
                device_cs = f"HostName={dotenv_values('.env')['HostName']};DeviceId={device.device_id};SharedAccessKey={device.authentication.symmetric_key.primary_key}"
                print(device.device_id, device_cs, twin.tags['device_type'], twin.tags)
                device_connection_strings.append((device.device_id, device_cs, twin.tags['device_type'] if twin.tags is not None else None))

            # Write all connection strings to the file
            with open("cached_connections.json", "w") as localCacheFile:
                json.dump(device_connection_strings, localCacheFile)

            return device_connection_strings

    #Fetch a type of devices
    def get_device_connection_strings_by_device_type(self,device_type=""):
        
        valid_connection_strings = [x for x in self.connection_pool if x[2] is not None and device_type.lower() in x[2].lower()]
        
        if len(valid_connection_strings) >= 1:
            val = self.connection_pool.pop(self.connection_pool.index(valid_connection_strings.pop()))
            return val
        else:
            #create a new sensor
            print("No more connections available,do you wish to create a new sensor? Y/N")
            response = input()
            if response.lower() in "no":
                print("Will not simulate any more devices")
                return (None,None)
            else:
                print("Creating new device...")
                new_device = self.create_device(f"{device_type.lower()}_{uuid.uuid4()}")
                return new_device 
        

    # Create a new device
    def create_device(self,device_id):
         # Create or get device
        try:
            new_device = self.registry_manager.create_device_with_sas(device_id, primary_key=None,secondary_key=None, status="enabled")
            print(f"Created device {device_id}")
        except Exception as e:
            # Device might already exist, try getting it instead
            print(f"Device {device_id} creation failed, trying to retrieve it instead. Error: {e}")
            new_device = self.registry_manager.get_device(device_id)
        
        # Construct connection string
        device_cs = f"HostName={dotenv_values('.env')['HostName']};DeviceId={new_device.device_id};SharedAccessKey={new_device.authentication.symmetric_key.primary_key}"
        # Check if the device is ready and enabled
        print("Waiting for device to be enabled. Please enable the device in the respective IoTHub")
        while True:
            print("Attempting connection...")
            new_device = self.registry_manager.get_device(device_id)
            if new_device and new_device.status == "enabled":
                break
            time.sleep(10)
        # Check device state (enabled/disabled)
        if new_device.status == 'enabled':
            print(f"Device {device_id} is enabled and ready to connect.")
            return new_device.device_id, device_cs
        else:
            print(f"Device {device_id} is not enabled. Please check the device status in the IoT Hub.")
            return (None, None)
