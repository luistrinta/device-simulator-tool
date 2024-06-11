from azure.iot.device import Message
import random
import json 
import datetime


class V1():
  
  MSG_TXT = '{{"T":{temperature},"H":{humidity},"time":{time},"meta":{meta}}}'

  name = "Energy Sensor"
  def generate_telemetry(outlier=False):
      
      ivl1= 200000 +  random.randint(0,38600)
      ivl2= 200000 +  random.randint(0,40600)
      ivl3= 200000 +  random.randint(0,35900)
      icl1= 10000 +  random.randint(0,7942)
      icl2= 4000 +  random.randint(0,2500)
      icl3= 5000 +  random.randint(0,945)
      ipl1= 4100000 +  random.randint(0,13000)
      ipl2= 1400000 +  random.randint(0,17000)
      ipl3= 1100000 +  random.randint(0,31000)
      iprl1= -750000 +  random.randint(0,2000)
      iprl2= -400000 -  random.randint(0,100000)
      iprl3= -703000 - random.randint(0,10000)
      ipfl1= 900 + random.randint(0,100)
      ipfl2= 900 + random.randint(0,100)
      ipfl3= 800 + random.randint(0,100)
      ipr=  random.randint(-30000,-20000)
      ip= ipr*(-2)
      ipf= 934
      cei= 38073720
      ceir= 10
      cee= 0
      ceer= 2346598
      time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        
    
      MSG_TXT = { 
      "ivl1": ivl1,
      "ivl2": ivl2,
      "ivl3": ivl3,
      "icl1": icl1,
      "icl2": icl2,
      "icl3": icl3,
      "ipl1": ipl1,
      "ipl2": ipl2,
      "ipl3": ipl3,
      "iprl1": iprl1,
      "iprl2": iprl2,
      "iprl3": iprl3,
      "ipfl1": ipfl1,
      "ipfl2": ipfl2,
      "ipfl3": ipfl3,
      "ivln": None,
      "i":None,
      "ip": ip,
      "ipr": ipr,
      "ipf": ipf,
      "cei": cei,
      "ceir":ceir,
      "cee": cee,
      "ceer": ceer,
      "f": 50,
      "time": time,
      "meta": {
            "company": "DEV",
            "protocol_version":1,
            "device_type":"EOT-SGE"
        }
      }
      if False:
          MSG_TXT = { 
      "ivl1": ivl1/100,
      "ivl2": ivl2/100,
      "ivl3": ivl3/100,
      "icl1": icl1/100,
      "icl2": icl2/100,
      "icl3": icl3/100,
      "ipl1": ipl1/100,
      "ipl2": ipl2/100,
      "ipl3": ipl3/100,
      "iprl1": iprl1/100,
      "iprl2": iprl2/100,
      "iprl3": iprl3/100,
      "ipfl1": ipfl1/100,
      "ipfl2": ipfl2/100,
      "ipfl3": ipfl3/100,
      "ivln": None,
      "i":None,
      "ip": ip/100,
      "ipr": ipr/100,
      "ipf": ipf/100,
      "cei": cei/100,
      "ceir":ceir/100,
      "cee": cee/100,
      "ceer": ceer/100,
      "f": 50/100,
      "time": time,
      "meta": {
            "company": "DEV",
            "protocol_version":1,
            "device_type":"EOT-SGE"
        }
      }
  
    
      return Message(json.dumps(MSG_TXT))