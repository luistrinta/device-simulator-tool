import json
import os
from simulator.device import Device
from iothub import iot_hub_manager
import threading

class DeviceManager():
    
    #------------------------------Constructor------------------------------
    def __init__(self):
        # Path to the current file (e.g., module_file.py inside your module)
        current_file_path = os.path.abspath(__file__)

        # Directory of the current file
        current_directory = os.path.dirname(current_file_path)

        # Path to secret.json relative to the current file
        json_file_path = os.path.join(current_directory, 'secret.json')

        # Now, you can open the file
        with open(json_file_path, 'r') as file:
            self.mappings = json.load(file)
            file.close()
            
        # We map each module to the respective sensor    
        self.sensor_mapping = setup_dictionary()
        self.thread_list = []
        self.device_pool = {}  
        self.iot_hub_manager = iot_hub_manager.IotHubManager()              
        
    #------------------------------Start devices------------------------------
    def start_single_device(self,device_type="ENERGY_V1",interval_s=20):
        print(f"Starting sensor {device_type}. Sending messages every {interval_s} seconds")
        
        device_connection_string = self.iot_hub_manager.get_device_connection_strings_by_device_type(device_type.split("_")[0])
        
        print(device_connection_string)
        
        if device_connection_string[0] is None or device_connection_string[1] is None:
            return
        else:
            device = Device(
                            device_connection_string=device_connection_string[1],
                            sensor_name=device_connection_string[0],
                            device_type=self.sensor_mapping[device_type.lower()],
                            interval_s=interval_s
                            )
        
            
            t = threading.Thread(target=device.start)
            t.daemon=True
            self.thread_list.append((t,device))
            t.start()
            
    
    def start_multiple_devices(self,sensor_list,interval_s =20):
         for sensor in sensor_list:
          
            if sensor.lower().split("_")[0] not in list(self.mappings.keys()):
                print(f"Parsing Error: Nome de sensor inválido -> {sensor}")
                return
            else:
                self.start_single_device(device_type=sensor.lower(),
                                        interval_s=interval_s)
                print(f"Device of type {sensor} started successfully")  
                      
    #------------------------------Stop devices------------------------------
    def stop_all_devices(self):
        for thread,device in self.thread_list:
            device.stop()
           
#------------------------------Auxiliar methods------------------------------            
def setup_dictionary():
    dict = {}
    #import sensor modules
    from sensors import default 
    from sensors import temperature
    from sensors import airquality
    from sensors import energy
    from sensors import gas
    from sensors import water
    from sensors import tempext
    from sensors import fuel
    
    #define a dictionary
    dict["default"] = default
    dict["temperature_v1"] = temperature.V1   
    dict["temperature_v2"] = temperature.V2 
    dict["temperature_v3"] = temperature.V3 
    dict["airquality_v1"] = airquality.V1 
    dict["airquality_v2"] = airquality.V2 
    dict["airquality_v3"] = airquality.V3 
    dict["energy_v1"] = energy.V1 
    dict["gas_v1"] = gas.V1 
    dict["water_v1"] = water.V1
    dict["tempext_v1"] = tempext.V1
    dict["fuel_v1"] = fuel.V1
    
    return dict                        