import paho.mqtt.client as mqtt
import json
import BMS_test
import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler
from queue import Queue
from queue import Queue

# MQTT 服务器信息
broker_address = "10.8.6.26"
broker_port = 1893
username = "chibi01"
password = "chibi@!!"

# 全局变量
id = 0
cnt = 0
queue = Queue()

# 回调函数：连接成功时触发
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("连接成功！")
    else:
        print(f"连接失败，错误码：{rc}")

# 回调函数：接收到消息时触发
def on_message(client, userdata, msg):
    print(f"收到消息：{msg.topic} {msg.payload.decode()}")

# 发送消息的函数
def publish_message(client_id):
    global id
    id += 1
    base="sky"
    client_id= f"{base}{str(id).zfill(3)}"
    print(client_id)
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, broker_port, 60)
    client.loop_start()

    try:
        json_string = json.dumps(BMS_test.test_report())
        topic = "mqtt/server/status/up"
        result = client.publish(topic, json_string)
        status = result[0]
        if status == 0:
            client.loop_stop()
            client.disconnect()
            #print(f"Send `{json_string}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        #time.sleep(1)

    except KeyboardInterrupt:
        print("\nDisconnecting from MQTT Broker...")
        client.loop_stop()
        client.disconnect()
        print("Disconnected")

# 多线程任务


# queue = Queue()

# def worker():
#     while True:
#         task = queue.get()
#         if task is None:
#             break
#         task()
#         queue.task_done()

# 创建一个工作线程




def task():
    global cnt
    threads = []
    start_time = time.time()
    for i in range(5):
        cnt += 1
        queue.put(lambda: publish_message(f"sky{str(cnt).zfill(3)}"))
    end_time = time.time()
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")
    print(f'{cnt} 个请求成功')

# 定时任务
def scheduled_task():
    s = 1
    while s < 5:
        #print(f"第{s}次请求发送")
        s += 1
        task()
    
    # 等待所有任务完成


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, 'interval', seconds=1,max_instances=1)
    scheduler.start()
    try:
        s=1
        while s<2:
            #print(f"第{s}次请求发送")
            s+=1
            time.sleep(1)
        print('Exit')
    except (KeyboardInterrupt, SystemExit):
        
        scheduler.shutdown()













