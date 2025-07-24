
id=1000
WEB_PRODUCT_KEY = "2925b78dea884f78bae016b17f7f3606"
WEB_PRODUCT_SECRET = "F1361D92446B4759849EF7EB98458872"

import json
import base64
import hashlib
import time
import re

deviceNo="0F"
def generate_sign():  
    global id
    id+=1
    base="0F"
    deviceNo= f"{base}{str(id).zfill(11)}" 
    product = {   #// 产品Key --必传
    "productKey":"2925b78dea884f78bae016b17f7f3606", #//支持数字、小写字母，长度等于32位
    
    #// 设备编号  --必传
    "deviceNo":"0F00000001471",   
    #// 设备版本  --必传
    "deviceVersion":"v1.0.1"   }
    product["deviceNo"] = deviceNo

    print(product["deviceNo"])
    json_str = json.dumps(product)
    
    

    #     # 对JSON字符串进行Base64编码
    data = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    

    #     # 获取当前时间戳
    timestamp = int(time.time() * 1000)

    #     # 生成签名
    sign_str = data + str(timestamp) + WEB_PRODUCT_KEY + WEB_PRODUCT_SECRET
    sign = hashlib.sha1(sign_str.encode('utf-8')).hexdigest()

    #     # 创建包含签名和其他信息的字典
    obj = {
            "data": data,
            "timestamp": str(timestamp),
            "sign": sign,
            "productKey": WEB_PRODUCT_KEY
        }

    #     # 将字典转换为JSON字符串并打印
    obj_str = json.dumps(obj)
    return obj_str
if __name__=='__main__':
    for i in range(1000):
        print(generate_sign())
