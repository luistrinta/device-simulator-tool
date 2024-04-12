from azure.iot.device import Message
import random
import json 
import datetime

class V1():

    name = "Temperature LIKE '7%' Sensor"
    def generate_telemetry():
        message={
            "device": "7B0CF7",
            "data": "31bd60682606826068260682",
            "seqNumber": 1123,
            "model_type": 3,
            "config_mode": 1,
            "volt" : 50 + random.randint(0,150),
            "p0" : 200 + random.randint(200,300),
            "p2" : 200 + random.randint(200,300),
            "time" : int(datetime.datetime.now().timestamp()),
            "p4" : 200 + random.randint(200,300),
            "p6" : 200 + random.randint(200,300),
            "p1" : 200 + random.randint(200,300),
            "p3" : 200 + random.randint(200,300),
            "p5": 200 + random.randint(200,300),
            "p7" : 200 + random.randint(200,300)
            }
       
       
        
        return Message(json.dumps(message))

class V2():
    name = "Temperature LIKE 'Amb%' Sensor"
    def generate_telemetry():
        temperature = 0 + random.randint(-30, 10)
        message={
            "T": None if temperature < 0 else temperature,
            "volt" : 50 + random.randint(0,150)
            }
       
       
        
        return Message(json.dumps(message))

class V3():
    
    name = "Temperature V3 Sensor"
    def generate_telemetry():
        
        temperature = 0 + random.randint(-30, 10)
        humidity = 10 + random.randint(20,80)
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        
        if humidity < 70:    
            message = {
                "T":temperature,
                "H":humidity,
                "time":time,
                "meta":{
                    "company": "DEV",
                    "protocol_version":1,
                    "device_type":"Temp"
                }
            }
        else:
            message = {
                "T":temperature,
                "H":None,
                "time":time,
                "meta":{
                    "company": "DEV",
                    "protocol_version":1,
                    "device_type":"Temp"
                }
            }
        
        return Message(json.dumps(message))