from azure.iot.device import Message
import random
import json 
import datetime



class V1():
    name="Fuel Type"
    
    def generate_telemetry():
        fuel_start = 1000 -random.randint(0,1000)
        time = int(datetime.datetime.now().timestamp())
        vbat= 4561
        csq = random.randint(0,31)
        message={
                    
            "data": {
                "data_channel_1": [
                    {
                        "ts": time,
                        "measure(mA*100)": fuel_start
                    }
                ],
                "write_key": "13C193B1DB0558E7",
                "vbat": vbat,
                "csq": csq,
                "msg_totalizer": 0
            },
            "meta": {
               "company": "MO_SONAE",
               "protocol_version": 1,
               "probe": "4-20",
               "device_type": "Genoa_4_20"
            }
        }
        
        
        return Message(json.dumps(message))