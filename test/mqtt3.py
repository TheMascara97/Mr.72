import paho.mqtt.client as mqtt
import json
import BMS_test
import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler
from queue import Queue

# MQTT 服务器信息
broker_address = "10.8.6.26"
broker_port = 1893
username = "chibi01"
password = "chibi@!!"

# 全局变量
id = 0
cnt = 0

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
    with thread_lock:  # 使用锁保护共享变量的访问
        id += 1
    base = "sky"
    client_id = f"{base}{str(id).zfill(3)}"
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
            # print(f"Send `{json_string}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        # time.sleep(1)

    except KeyboardInterrupt:
        print("\nDisconnecting from MQTT Broker...")
        client.loop_stop()
        client.disconnect()
        print("Disconnected")

# 多线程任务
def task():
    global cnt
    threads = []
    start_time = time.time()
    for i in range(5):
        with thread_lock:  # 使用锁保护共享变量的访问
            cnt += 1
        queue.put(lambda: publish_message(f"sky{str(cnt).zfill(3)}"))  # 将任务添加到队列

    # 等待队列中的所有任务完成
    queue.join()
    end_time = time.time()
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")
    print(f'{cnt} 个请求成功')

# 定时任务
def scheduled_task():
    s = 1
    while s < 5:
        print(f"第{s}次请求发送")
        # id = 0  # 如果需要重置id，取消注释
        s += 1
        queue.put(task)  # 将任务添加到队列

# 创建线程锁
thread_lock = threading.Lock()

# 创建队列
queue = Queue()

# 工作线程函数
def worker():
    while True:
        task_func = queue.get()
        if task_func is None:
            break
        task_func()  # 执行任务
        queue.task_done()

# 创建工作线程
worker_thread = threading.Thread(target=worker)
worker_thread.start()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, 'interval', seconds=1)
    scheduler.start()
    try:
        s = 1
        while s < 2:
            s += 1
            time.sleep(1)
        print('Exit')
    except (KeyboardInterrupt, SystemExit):
        # 停止工作线程
        queue.put(None)
        worker_thread.join()
        scheduler.shutdown()