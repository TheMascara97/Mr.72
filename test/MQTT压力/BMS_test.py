import selenium
import requests
import json
import requests  
import json
import hashlib
import subprocess  
import platform  
import json
import SIGN
import time
import os
import time  
from datetime import datetime  
import MQTT1
import threading
id=0




def test_update():
    global id
    id+=1
    base="sky"
    deviceNo= f"{base}{str(id).zfill(3)}"
    json_data = {
  "deviceId":"FFFFFFFFFF7313254",
  "timestamp": 1728530320343,
  "data": {
    "taskId":32,
    "upStatus":2,
    "errorCode":0,
    "version":"v1.0.3-1.0.20"
  }
} 
    json_data["deviceId"] = deviceNo

    # print(json_data["deviceId"])  
    # print(json_data)
    #     # 将产品信息转换为JSON字符串
   
    return json_data

def test_report():
    global id
    id+=1
    if id<=600:
        base="sky"
        deviceNo= f"{base}{str(id).zfill(3)}"
        json_data =  {"deviceId": "sky002", "locationLng": "",
                      "timestamp": 1749024605, "iccid": "898608631025D0346232", "imei": "862635067313254", "locationLat": "",
                      "data": [{"happenTime": 1749024605, "content": ["14.575", "13.677", "1724", "1725", "1725", "1725", "1726", "1725", "1724", "1724", "-0.130", "53", "4", "100", "418", "422", "200", "-40", "-40", "-40", "1.726", "1.724", "5", "1", "0", "25", "25", "25", "25", "25", "7", "0", "0", "0", "00000000", "v1.0.3-1.0.1", "1.0.1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "21"]}]}
        json_data["deviceId"] = deviceNo

        #print(json_data["deviceId"])
        #print(json_data)
    #     # 将产品信息转换为JSON字符串
   
        return json_data
    else:
        id=0
        id+=1
        base="sky"
        deviceNo= f"{base}{str(id).zfill(3)}"
        json_data =  {"deviceId": "sky002", "locationLng": "",
                      "timestamp": 1749024605, "iccid": "898608631025D0346232", "imei": "862635067313254", "locationLat": "",
                      "data": [{"happenTime": 1749024605, "content": ["14.575", "13.677", "1724", "1725", "1725", "1725", "1726", "1725", "1724", "1724", "-0.130", "53", "4", "100", "418", "422", "200", "-40", "-40", "-40", "1.726", "1.724", "5", "1", "0", "25", "25", "25", "25", "25", "7", "0", "0", "0", "00000000", "v1.0.3-1.0.1", "1.0.1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "21"]}]}
        json_data["deviceId"] = deviceNo

        #print(json_data["deviceId"])

        return json_data
