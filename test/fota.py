import requests  
import json
import hashlib
import subprocess  
import platform  

import subprocess
import time
import os
import time  
from datetime import datetime  
  

down_file_path = 'E:\\SC5000\\fota_test\\down\\ota.swu' 
up_file_path = 'E:\\SC5000\\fota_test\\up\\ota.swu' 
up_version = '1.0.2'
down_version = '1.0.1'

token_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Token%22,%22param%22:{%22action%22:%22token%22}}'  
get_fota_version_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Upgrade%22,%22param%22:{%22action%22:%22fw_version%22,%22is_loading%22:false}}'  
get_version_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Device%22,%22param%22:{%22action%22:%22version%22}}'  
login_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=Login&{%22module%22:%22Login%22,%22param%22:[%22admin%22,%2221232f297a57a5a743894a0e4a801fc3%22]}' 
current_slot_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22SIM%22,%22param%22:{%22action%22:%22sim_current_solt%22}}'  
set_slot_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=SetParameter'
connect_state_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Internet%22,%22param%22:{%22action%22:%22connect_status%22}}'
set_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=SetParameter'

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
    contend,code = get_request_json(token_url)
    if contend.get("error") == 0:
        return contend.get("param").get("services_param").get("token"),code
    else:
        return 0,code
def get_up_staus(url="http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Upgrade%22,%22param%22:{%22action%22:%22upgrade_status%22}}"):
        # 发送 GET 请求  
    contend,code = get_request_json(url)
    if contend.get("error") == 0:
        return contend.get("param").get("upgrade_param").get("state")
    else:
        return 0,code

def check_version():
    contend,code = get_request_json(get_fota_version_url)
    # print(contend)
    if contend.get("error") == 0:
        return contend.get("param").get("upgrade_param").get("version"),code
    else:
        return 0,code
def get_version():
        contend,code = get_request_json(get_version_url)
        if contend.get("error") == 0:
            return contend.get("param").get("device_param").get("firmware_version"),code
        else:
            return 0,code
    
    
def download(url,token):
    params = {
        "module": "Upgrade",
        "param": {
            "action": "fw_download"

        },
        "token": token
    }
    response = requests.post(url, json=params) 
    json_data = json.loads(response.content)
    if json_data.get("error")==0:
        return 1
    else:
        return -1


def download_percent():
    contend,code = get_request_json("http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Upgrade%22,%22param%22:{%22action%22:%22fw_state%22}}")
    print(contend)
    if contend.get("error") == 0:
        return contend.get("param").get("upgrade_param").get("state")
    else:
        return 0,code
def upgrade(url,token):
    params = {
        "module": "Upgrade",
        "param": {
            "action": "fw_ota"

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
import requests  
  
def reboot(url, token):  
    params = {  
        "module": "Device",  
        "param": {  
            "action": "reboot_device"  
        },  
        "token": token  
    }  
      
    try:  
        response = requests.post(url, json=params)  
        response.raise_for_status()  # 确保响应状态码是 2xx  
        json_data = response.json()  # 直接使用 .json() 方法  
  
        if json_data.get("error") == 0:  
            return 1  
        else:  
            return -1  
    except requests.exceptions.ConnectionError as e:  
        # 处理所有连接相关的错误  
        print(f'连接错误: {e}') 
        token,http_code = get_token(token_url) 
    # finally:
    #     time.sleep(20)
    #     token,http_code = get_token(token_url)

def ping_host(ip_address="192.168.1.1"):
    # 根据操作系统选择正确的ping命令
    if os.name == 'nt':  # Windows
        command = ['ping', '-n', '1', ip_address]
    else:  # Linux and macOS
        command = ['ping', '-c', '1', ip_address]

    return subprocess.call(command) == 0
        
def fota_upgrade():
    token,http_code = get_token(token_url)
    print(token,http_code)
    time.sleep(2)
    # 检查版本
    version = check_version()[0]
    
    print("next version:",version)
    time.sleep(5)
    token,http_code = get_token(token_url)
    # 下载
    print(download(set_url,token))
    while download_percent()!=2:
        time.sleep(5)
    token,http_code = get_token(token_url)
    print(upgrade(set_url,token))
    while get_up_staus()!=1:
        time.sleep(1)
    token,http_code = get_token(token_url)
    reboot(set_url,token)

    # finally:
    #     version=get_version()[0]
    


    #print(a)
    # a=get_version()[0]
    # print(a)

    




# fota_upgrade()
# print(get_version())       
if __name__=='__main__':
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    i=1
    while i<1001:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('------------------------------------第{}次测试------------------------------------------'.format(i))
        i+=1
        while True:
            if ping_host():
                print(f'Ping to was successful.')
                break
            else:
                print(f'Ping to failed, trying again...')
                time.sleep(5) 

        now_version=get_version()[0]
        print("now_version:",now_version)
        fota_upgrade()
        time.sleep(200) 
        while True:
            if ping_host():
                print(f'Ping to was successful.')
                break
            else:
                print(f'Ping to failed, trying again...')
                time.sleep(5)
        time.sleep(20) 
        
        version=get_version()[0]
    
        if version!=now_version and now_version!=0:
            print('升级成功')
            upgrade_result = 1
        else:
                print('升级失败')
                upgrade_result = 0
                # Log the result to the file
        with open(f'F:/code/fota_log/{year}{month}{day}_result', 'a', encoding="utf-8") as file: 
            if upgrade_result== 1 :
                file.write(f"{timestamp} 第 {i} 次升级成功\n")
            else:
                file.write(f"{timestamp} 第 {i} 次升级失败\n")
    





