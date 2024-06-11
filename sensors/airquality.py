import json
import random
import datetime
from azure.iot.device import Message

class V1():
  #old air quality sensor
  name = "Airquality Sensor"
  def generate_telemetry():
        message={
          "data": {
                    "year": datetime.datetime.now().year,
                    "month": datetime.datetime.now().month,
                    "day": datetime.datetime.now().day,
                    "csq": 15 + random.randint(3,20),
                    "pcpm25": random.randint(0,5),
                    "pcpm10": random.randint(0,5),
                    "co2": random.randint(200,450),
                    "tvoc": random.randint(300,700),
                    "temp": 10 + random.randint(5,15),
                    "rh": random.randint(40,70),
                    "created_at_unix_utc": int(datetime.datetime.now().timestamp()),
                    "created_at_day_utc": datetime.datetime.now().strftime("%Y%M%D")
                  },
          "meta": {
                    "company": "DEV",
                    "protocol_version": 1,
                    "probe": "AmbV1",
                    "device_type": "EOT-AirQ"
    }
        }
              
        
        return Message(json.dumps(message))

class V2():
   #Amb LIKE Sensor
    pass

class V3():
  name= "Airquality Sensor (QAT)"
  def generate_telemetry():
        message={
                  "pm2": random.randint(0,15),
                  "pm1": random.randint(0,10),
                  "pm10": random.randint(0,20),
                  "CO2": random.randint(200,450),
                  "TVOC": random.randint(300,700),
                  "T": 10 + random.randint(5,15),
                  "H": random.randint(40,70),
                  "time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                  
                  "meta": {
                            "company": "DEV",
                            "protocol_version": 2,
                            "device_type": "AirQ"
                          }
                  }
              
        
        return Message(json.dumps(message))
