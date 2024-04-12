from azure.iot.device import Message
import random
import json 
import datetime

class V1():
   name = "Gas Sensor"
   def generate_telemetry():
      delta_to_totalizer_1 = 3
      delta_to_totalizer_2 = 4
      delta_to_totalizer_3 = 3
      seqNumber = 1175
      totalizer = random.randint(2000,8000)
      time = int(datetime.datetime.now().timestamp())
         
      message = {
         "totalizer":totalizer,
         "delta_to_totalizer_1":delta_to_totalizer_1,
         "delta_to_totalizer_2":delta_to_totalizer_2,
         "delta_to_totalizer_3":delta_to_totalizer_3,
         "seqNumber":seqNumber,
         "time":time,
         "meta":{
            "company":"DEV",
            "protocol_version":1,
            "device_type":"EOT-GAS"
         }
      }
      
      return Message(json.dumps(message))