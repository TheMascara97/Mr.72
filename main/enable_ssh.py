import requests  
import json
import hashlib
import subprocess  
import platform  


import time
import os
import time  
from datetime import datetime  
import get_ip
  

down_file_path = 'E:\\SC5000\\fota_test\\down\\ota.swu' 
up_file_path = 'E:\\SC5000\\fota_test\\up\\ota.swu' 
up_version = '1.0.2'
down_version = '1.0.1'

def process_string():
    # 检查字符串长度是否至少为10
    if len(get_ip.desired_ip()) < 10:
        return "字符串长度不足10,无法处理"
    
    # 获取第十位（索引为9）
    tenth_char1 = get_ip.desired_ip()[9]
    tenth_char2 = get_ip.desired_ip()[10]
    
    # 判断第十位是否为数字
    if tenth_char1.isdigit():
        # 如果是数字，取前11位
        if tenth_char2.isdigit():
            result = get_ip.desired_ip()[:12]
        else:
            result = get_ip.desired_ip()[:11]
    else:
        # 如果不是数字，取前10位
        result = get_ip.desired_ip()[:10]
    
    return result
    
def now_url():
    
    now_url=process_string()
    
    base_ip = f'{now_url}1'
    token_url = f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Token%22,%22param%22:{%22action%22:%22token%22}}"
    login_url = f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=Login&{%22module%22:%22Login%22,%22param%22:[%22admin%22,%2221232f297a57a5a743894a0e4a801fc3%22]}"
    current_slot_url =f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22SIM%22,%22param%22:{%22action%22:%22sim_current_solt%22}}"
    set_slot_url = f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=SetParameter"
    connect_state_url = f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Internet%22,%22param%22:{%22action%22:%22connect_status%22}}"
    set_url =f"http://{base_ip}"+"/cgi-bin/mycgi.cgi?ACT=SetParameter"
    return base_ip,token_url,login_url,current_slot_url,set_slot_url,connect_state_url,set_url

def get_request(url):
        # 发送 GET 请求  
    response = requests.get(url)  
    return response.content,response.status_code

def get_request_json(url, max_retries=10, retry_delay=2):  
    retries = 0  
    while retries < max_retries:  
        response = requests.get(url)  
        try:  
            data = json.loads(response.content)  
            return data, response.status_code  
        except json.JSONDecodeError:  
            print(f"Json解码失败:重试请求")  
            retries += 1  
            if retries < max_retries:  
                time.sleep(retry_delay)  # 等待一段时间后再重试  
      
    # 如果达到最大重试次数，则返回None和响应状态码  
    return None, response.status_code  

def get_token(url):

        # 发送 GET 请求  
    contend,code = get_request_json(now_url()[1])
    if contend.get("error") == 0:
        return contend.get("param").get("services_param").get("token"),code
    else:
        return 0,code


def control_ssh(url,token,enable):
    params = {
        "module": "EnginnerTool",
        "param": {
            "action": "ssh",
            "services_param": {
                "enable": enable
            }
        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1
def control_adb(url,token,enable):
    params = {
        "module": "EnginnerTool",
        "param": {
            "action": "usb_adb",
            "services_param": {
                "enable": enable
            }
        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1
def factory_restore(url,token):
    params = {
        "module": "Device",
        "param": {
            "action": "factory_restore"
           
        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1 
def reboot(url,token):
    params = {
        "module": "Device",
        "param": {
            "action": "reboot_device"
           
        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1
def ARMLOG(url,token):

    params = {
        "module": "EnginnerTool",
        "param": {
            "action":"nat_command_send","services_param":{"at_command":"AT+armlog: 1"
        }},
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1

def choose_slot(url,token,slot):
    params = {
        "module": "SIM",
        "param": {
            "action": "sim_current_solt",
            "SIM_param": {
                "current_solt": slot
            }
        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1

def get_connect_state(url):
    data , code = get_request_json(url)
    if data.get("error")==0:
        state = data.get('param').get('internet_param').get('status')
        if state == "connect":
            return 1
        else:
            return 0
        
# def set_connect(url,token):
#     params = {
#         "module": "Internet",
#         "param": {
#             "action": "manual_connect",
#             "internet_param": {
#                 "action": "connect"
#             }
#         },
#         "token": token


def ping_host(ip_address):
    # 根据操作系统选择正确的ping命令
    if os.name == 'nt':  # Windows
        command = ['ping', '-n', '1', ip_address]
    else:  # Linux and macOS
        command = ['ping', '-c', '1', ip_address]

    return subprocess.call(command) == 0

def main_SSH():
    token_url=now_url()[1]
    set_url=now_url()[6]
    ip_address = now_url()[0]
    while True:
        if ping_host(ip_address):
            print(f'Ping to {ip_address} was successful.')
            break
        else:
            print(f'Ping to {ip_address} failed, trying again...')
            time.sleep(5)  # 等待5秒后再次尝试
    time.sleep(2)  # 等待5秒后再次尝试
    token,http_code = get_token(token_url)
    print(token,http_code)
    control_ssh(set_url,token,1)

def main_ARMLOG():
    token_url=now_url()[1]
    set_url=now_url()[6]
    ip_address = now_url()[0]
    token,http_code = get_token(token_url)
    while True:
        if ping_host(ip_address):
            print(f'Ping to {ip_address} was successful.')
            break
        else:
            print(f'Ping to {ip_address} failed, trying again...')
            time.sleep(5)  # 等待5秒后再次尝试
    print(token,http_code)
    ARMLOG(set_url,token)

def main_ADB():
    token_url=now_url()[1]
    set_url=now_url()[6]
    ip_address = now_url()[0]
    while True:
        if ping_host(ip_address):
            print(f'Ping to {ip_address} was successful.')
            break
        else:
            print(f'Ping to {ip_address} failed, trying again...')
            time.sleep(5)  # 等待5秒后再次尝试
    time.sleep(2)  # 等待5秒后再次尝试
    token,http_code = get_token(token_url)
    print(token,http_code)
    
    adb=control_adb(set_url,token,1)
    if adb==1:
        main_reboot()
        
    
def main_reset():
    token_url=now_url()[1]
    set_url=now_url()[6]
    token,http_code = get_token(token_url)
    print(token,http_code)
    factory_restore(set_url,token)
def main_reboot():
    token_url=now_url()[1]
    set_url=now_url()[6]
    token,http_code = get_token(token_url)
    print(token,http_code)
    reboot(set_url,token)


#main_SSH()
#main_reset()
#main_reboot()
#main_ADB()


