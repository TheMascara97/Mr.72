import requests  
import json
import hashlib
import subprocess  
import platform  
import time  
from datetime import datetime  
  

down_file_path = 'E:\\SC5000\\fota_test\\down\\ota.swu' 
up_file_path = 'E:\\SC5000\\fota_test\\up\\ota.swu' 
up_version = '1.0.2'
down_version = '1.0.1'
base_ip="192.168.1.1"
token_url = 'http://192.168.1.1/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Token%22,%22param%22:{%22action%22:%22token%22}}'  
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

def post_request_json(url, params,max_retries=10, retry_delay=2):  
    retries = 0  
    while retries < max_retries:  
        response = requests.post(url,json=params)  
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
    json_data,code = post_request_json(url,params)
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
class SSH:
    
    def __init__(self):
        import paramiko
        
        self.ssh = paramiko.SSHClient()
 
# 允许连接不在know_hosts文件中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        name=f'{base_ip}'
# 连接服务器
        self.ssh.connect(hostname=name, port=22, username='root', password='quectel')
    def get_infomation(self,code1,code2,code3):
       
        stdin, stdout, stderr = self.ssh.exec_command(code1)
        info1=stdout.read().decode('UTF-8')
        print(info1,end="")
        stdin, stdout, stderr = self.ssh.exec_command(code2)
        info2=stdout.read().decode('UTF-8')
        print(info2,end="")
        stdin, stdout, stderr = self.ssh.exec_command(code3)
        info3=stdout.read().decode('UTF-8')
        print(info3,end="")
    def get_ICCID(self):

            stdin, stdout, stderr = self.ssh.exec_command('skysoft_client get_iccid')

            result=stdout.read().decode('UTF-8')

            # print(result,end="")
            if result !="":
                 return result
            else:
                 return "无内置卡"      




    
# print(SSH().get_ICCID())
with open('test_results.txt', 'a', encoding='utf-8') as file: 
        file.write("----------------------------------------------------\n")  
        for j in range(1,10000):
            second=0
            result=0
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file.write(f"{timestamp}----------------第{j}次测试开始-------------------------------\n")
            start_time = time.time()  
            contend,code = get_request_json(login_url)
            token,code = get_token(token_url)
            data , code = get_request_json(current_slot_url)
            current_slot = data.get("param").get('SIM_param').get('current_solt')
            file.write(f"当前卡槽为:{current_slot}")
            

            choose_slot(set_slot_url,token,1)
            file.write(f"\n准备切换到卡槽为:1\n")
            print("准备切换到卡槽为:1\n")
            time.sleep(30)
            file.write(SSH().get_ICCID())
            time.sleep(2)
            choose_slot(set_slot_url,token,2)
            file.write(f"\n准备切换到卡槽为:2\n")
            print("准备切换到卡槽为:2\n")
            time.sleep(30)
            file.write(SSH().get_ICCID())
            time.sleep(2)
            choose_slot(set_slot_url,token,3)
            file.write(f"\n准备切换到卡槽为:3\n")
            print("准备切换到卡槽为:3\n")
            time.sleep(30)
            file.write(SSH().get_ICCID())
            time.sleep(2)
            choose_slot(set_slot_url,token,4)
            file.write(f"\n准备切换到卡槽为:4\n")
            print("准备切换到卡槽为:4\n")
            time.sleep(30)
            file.write(SSH().get_ICCID())
            time.sleep(2)

            # # 等待设备稳定
            # time.sleep(5)
            # for i in range(1,120):
            #     if get_connect_state(connect_state_url):
            #         result = "成功"
            #         second = i
            #         break
            #     else:
            #         second=i
            #         result = "失败"
            #     time.sleep(1)
            # time_difference  = time.time()-start_time
            # print(f"第{j}次测试{result} 切卡完成后->联网耗时({time_difference})")
            
                # # 这边到时候获取iccid吧
                # slot = data.get("param").get('SIM_param').get('current_solt')
                # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
                # output_string = f"{timestamp}:第{j}次测试 {result} 卡槽{current_slot}切换到卡槽{slot} 耗时({time_difference})\n" 
