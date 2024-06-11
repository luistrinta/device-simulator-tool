from azure.iot.device import Message
import random
import json 
import datetime



class V1():
    name="Fuel Type"
    
    def generate_telemetry():
        fuel_start = 1000 -random.randint(0,750)
        time = datetime.datetime.now()
        vbat= 4561
        csq = random.randint(0,31)
        array_of_registers = []
        is_full_resquest = random.randint(0,23) > 22
        if not is_full_resquest:
            array_of_registers.append({"ts": int(time.timestamp()), "measure(mA*100)": fuel_start})
        else:
            for i in range(0,23):
                        array_of_registers.append({"ts": int(time.timestamp()), "measure(mA*100)": fuel_start})
                        fuel_start = fuel_start -random.randint(0,10)
                        time = time - datetime.timedelta(hours=1)
                        print(time)
        message={
                    
            "data": {
                "data_channel_1": array_of_registers,
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
    
    
    