from azure.iot.device import Message
import random
import json 
import datetime

class V1():

    name = "Default Sensor"
    def generate_telemetry():
        temperature = 0 + random.randint(-30, 10)
        humidity = 0 + random.random()*80
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
        meta =json.dumps(
                {
                "company": "DEV",
                "protocol_version":1,
                "device_type":"Temp"
            }
                , sort_keys=True)
            
        MSG_TXT = '{{"T":{temperature},"H":{humidity},"time":{time},"meta":{meta}}}'
        
        msg_txt_formatted = MSG_TXT.format(temperature=temperature,humidity=humidity,time=time,meta=meta)
        
        return Message(msg_txt_formatted)