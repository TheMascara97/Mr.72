import requests  
import json
import hashlib
import subprocess  
import platform  


import time
import os
import time  
from datetime import datetime  

  


    
def now_url():
    
    
    
    base_ip = f'192.168.81.1'
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
    


def set_wan(url,token):
    params = {
        "module": "Lan",
        "param": {
            "action": "set_wan","lan_param":{"is_static_config":0,"link_backup_mode":1,"net_source_priority":1,"auto_dns":1,"dns":"120.133.231.107","dns_backup":"10.7.48.1"}},
           
        
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1 
def set_wan2(url,token):
    params = {
        "module": "Lan",
        "param": {
            "action": "set_wan","lan_param":{"is_static_config":0,"link_backup_mode":0,"net_source_priority":1,"auto_dns":1,"dns":"120.133.231.107","dns_backup":"10.7.48.1"}},
           
        
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1 
    # print(json_data)


def ping_host(ip_address):
    # 根据操作系统选择正确的ping命令
    if os.name == 'nt':  # Windows
        command = ['ping', '-n', '1', ip_address]
    else:  # Linux and macOS
        command = ['ping', '-c', '1', ip_address]

    return subprocess.call(command) == 0
    
def OPEN_WAN():
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
    a=set_wan(set_url,token)
    return a
def CLOSE_WAN():
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
    print(set_wan2(set_url,token))
    
    
    


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

def main_reboot():
    token_url=now_url()[1]
    set_url=now_url()[6]
    token,http_code = get_token(token_url)
    print(token,http_code)
    reboot(set_url,token)

if __name__ == "__main__": 
    
    i=1
    while True:  
        i+=1   
        print(f"第{i}次操作")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # CLOSE_WAN()
        # time.sleep(5)
        if OPEN_WAN()==1:
            time.sleep(5)
            print("操作成功")
            main_reboot()

            time.sleep(80)
            CLOSE_WAN()
            time.sleep(10)
        else:
            print(f"{timestamp} 操作失败")
            break

        
        


            # print("操作成功")

    # else:
    #     print(f"{timestamp} 操作失败")
    #     break