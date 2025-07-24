import paho.mqtt.client as mqtt
import json
import BMS_test
import threading
import atexit
# from Demos.FileSecurityTest import permissions_dir_inherit
# import win32security
from queue import Queue
import threading
id=0
cnt = 0
# MQTT服务器信息
# MQTT 代理服务器的配置
broker_address = "10.8.6.26"  # 公共 MQTT 代理服务器
broker_port = 1893  # 默认端口
#topic = "状态上报"  # 要发布消息的主题
username = "chibi01"  # 如果你的服务器需要用户名认证
password = "chibi@!!"  # 如果你的服务器需要密码认证
# client_id = "bms-sky001"

# 回调函数：连接成功时触发
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"连接成功！")
        return rc
        # 这里可以添加订阅主题的代码
        # client.subscribe("your/topic")
    else:
        print(f"连接失败，错误码：{rc}")

# 回调函数：接收到消息时触发
def on_message(client, userdata, msg):
    print(f"收到消息：{msg.topic} {msg.payload.decode()}")



# 
def publish_message(client_id):
    global id

    
    if id<600:
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
    else:
        id=0
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
#

        # 将JSON数据转换为字符串

        # json_string = json.dumps(BMS_test.test_report())

        #     # 发布JSON数据到MQTT主题
        # topic = "mqtt/server/status/up"  # 替换为你想要发布到的主题
        # client.publish(topic, json_string)
        # # print(f"已发布JSON数据到主题 '{topic}': {json_string}")

        #     # 等待一段时间以确保消息发送完成
        # import time
        # #time.sleep(1)
        # client.loop_stop()

def task():
        global cnt
        global id

        threads = []
        start_time = time.time()
        for i in range(600):
            cnt+=1
            thread =threading.Thread(target=publish_message, args=(f"sky{str(cnt).zfill(3)}",))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join() 
        end_time = time.time()
        print(f"All tasks completed in {end_time - start_time:.2f} seconds")
        # time.sleep(1)

        print(f'{cnt} 个请求成功')
        atexit.register(task)
if __name__ == '__main__':
    import atexit
    from apscheduler.schedulers.blocking import BlockingScheduler
    from datetime import datetime, timedelta
    import concurrent.futures
    import time
    s=1   # 创建 100 个线程

    while s<600:
        print(f"第{s}次请求发送")
        
        s+=1       
        task()
