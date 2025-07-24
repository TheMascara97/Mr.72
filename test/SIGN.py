import json
import base64
import hashlib
import time
import re



WEB_PRODUCT_KEY = "2925b78dea884f78bae016b17f7f3606"
WEB_PRODUCT_SECRET = "F1361D92446B4759849EF7EB98458872"
deviceNo="0F"
# def generate_device_no():
#     global start
#     start+=1
#     base="0F"
#     length=11
#     for i in range(start, start + 1):  # 假设生成 10 个设备编号
#         device_no = f"{base}{str(i).zfill(length)}"
#         device_no = str(device_no)
#         print (device_no)  
#         return (device_no)

id=4300
WEB_PRODUCT_KEY = "2925b78dea884f78bae016b17f7f3606"
WEB_PRODUCT_SECRET = "F1361D92446B4759849EF7EB98458872"

import json
import base64
import hashlib
import time
import re

deviceNo="0F"
def generate_sign1(): 
    global id
    id+=1
    base="0F"
    deviceNo= f"{base}{str(id).zfill(11)}" 
    product = {   #// 产品Key --必传
    "productKey":"2925b78dea884f78bae016b17f7f3606", #//支持数字、小写字母，长度等于32位
    
    #// 设备编号  --必传
    "deviceNo":"0F00000000002"  ,
    #// 设备版本  --必传
    "deviceVersion":"v1.0.1"   }
    product["deviceNo"] = deviceNo

    print(product["deviceNo"])  
    #     # 将产品信息转换为JSON字符串
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
    # obj_str = json.dumps(obj)
    # print(obj_str)
    # print(obj)
    return obj


def generate_sign2():  
    global id
    id+=1
    base="0F"
    deviceNo= f"{base}{str(id).zfill(11)}" 
    product = {   #// 产品Key --必传
    # "productKey":"273cf34a57c445bd940bd8fc77d37636", #//支持数字、小写字母，长度等于32位
    
    # #// 设备编号  --必传
    # "deviceNo":"0F00XK2800037",   
    # #// 设备版本  --必传
    # "deviceVersion":"v1.0.10"    
  

            #// 产品Key --必传
        "policyTaskId":73,
        #     #// 升级状态 --必传
            "upStatus":"UP_OK",
        #     UP_CHECK：检测到新版本、UP_START：升级开始、UP_OK：升级成功、UP_FAILED：升级失败
        #     #// 升级失败ErrorCode --必传
            "errorCode":0,   
        #     #// -1:升级失败 0:无异常 1:文件下载失败 2:文件校验失败

        #     #// 产品Key --必传
        "productKey":"2925b78dea884f78bae016b17f7f3606", 
        #     #//支持数字、小写字母，长度等于32位
        #     #// 设备编号  --必传
            "deviceNo":"0F00000001475",   
        #     #// 设备版本  --必传
            "deviceVersion":"v1.0.1"   
        }
    product["deviceNo"] = deviceNo

    # print(product["deviceNo"])  
    #     # 将产品信息转换为JSON字符串
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
    # print(obj_str)
    # print(obj)
    return obj
if __name__ == "__main__":
    import csv
    import json
    data_list = []
    for i in range(1500):
        
        

            a=generate_sign2()
            # b=json.dumps(a)
            data_list.append(a)
            # print(data_list)
    with open(f'C:/Users/Administrator/Desktop/json_data1.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for json_data in data_list:
                json_str = json.dumps(json_data)
                writer.writerow([json_str])


