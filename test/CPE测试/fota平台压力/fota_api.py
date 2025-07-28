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
check_version_url= "http://171.221.254.179:19090/apigw/ota/v0/client/check/version"
report_url="http://171.221.254.179:19090/apigw/ota/v0/client/report/up"
log_url="http://10.8.10.98:9090/api/v0/client/report/errorLog"



cnt = 0

def test_check_version():
    global cnt
    check_version_data=SIGN.generate_sign1()
    json_data =  json.dumps(check_version_data)
    response=requests.post(url=check_version_url,headers={'Content-Type': 'application/json'},data=json_data)
    # if response.status_code == 200:
    #     print('请求成功!')
    #     cnt = cnt + 1
    # else:
    #     print('请求失败，状态码:', response.status_code)

    

def test_report():
        global cnt
    # for i in range(10):
        report_date=SIGN.generate_sign2()
        json_data = json.dumps(report_date)
        response=requests.post(url=report_url,headers={'Content-Type': 'application/json'},data=json_data)
        # print("test:",report_date,report_url)

        if response.status_code == 200:
            # print('请求成功!')
            cnt = cnt + 1
        else:
            print('请求失败，状态码:', response.status_code)

# # 打印返回的JSON数据
#     print('返回的数据:')
#     print(json.dumps(response.json(), indent=4, ensure_ascii=False))

def test_log():
    log_data={
   #// 产品Key --必传
   "productKey":"2bfe98f803814cfdb7d7737b4f3eff22", 
   #// 任务ID --必传
   "policyTaskId":69,
   #// 设备编号 --必传"
   "deviceNo":"4444",   
   #// 日志文件 --必传
   #"file": hello.txt,
   #// 任务设备表关联ID  -- 必传
   "taskDeviceRelId":410 }  
    with open('hello.txt', 'rb') as file:   
        files = {'file': ('hello.txt', file, 'text/plain')}
        #json_data = json.dumps(log_data)
        response=requests.post(url=log_url,files=files,data=log_data)
    if response.status_code == 200:
        print('请求成功!')
    else:
        print('请求失败，状态码:', response.status_code)
    #files['file'].close()
# 打印返回的JSON数据

    #print(json.dumps(response.json(), indent=4, ensure_ascii=False))


import threading

if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    from datetime import datetime, timedelta
    import concurrent.futures
    import SIGN
    import time
    # 创建 100 个线程
    def task():
            
        threads = []
        start_time = time.time()

        for i in range(3):
            thread = threading.Thread(target=test_report)
            threads.append(thread)
            thread.start()
        end_time = time.time()
        print(f"All tasks completed in {end_time - start_time:.2f} seconds")
        time.sleep(5)

        print(f'{cnt} 个请求成功')

#     scheduler = BlockingScheduler()

# # 指定目标时间（例如：明天的 10:30）
#     target_time = datetime.now().replace(hour=14, minute=00, second=0, microsecond=0) + timedelta(days=0)

# # 添加任务
#     scheduler.add_job(task, 'date', run_date=target_time)

# # 启动调度器
#     scheduler.start()

    # test_report()
    # test_check_version()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
#         futures = []
#         for _ in range(5000):
#             futures.append(executor.submit(test_report))
        
#         # 等待所有任务完成
#         for future in concurrent.futures.as_completed(futures):
#             try:
#                 future.result()  # 获取任务结果
#             except Exception as e:
#                 print(f"Task generated an exception: {e}")

task()

# 创建调度器
