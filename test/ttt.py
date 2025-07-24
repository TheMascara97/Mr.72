import asyncio
import threading
import queue
import random
import time

# 同步队列示例
shared_queue = queue.Queue()

def producer():
    # 生产者函数，生成5个随机数作为项目，并放入队列中
    for _ in range(5):
        item = random.randint(1, 100)  # 随机生成1到100之间的数字
        shared_queue.put(item)  # 将项目放入队列
        print(f"Produced item: {item}")  # 打印生产的项目
        time.sleep(random.random())  # 随机延迟以模拟生产时间


def consumer():
    # 消费者函数，从队列中取出项目进行处理
    while True:
        item = shared_queue.get()  # 从队列中取出一个项目
        if item is None:
            break  # 如果取到None则退出循环
        print(f"Consumed item: {item}")  # 打印消费的项目
        time.sleep(random.random())  # 随机延迟以模拟处理时间
    shared_queue.task_done()  # 告诉队列此任务已完成


# 异步队列示例
async def async_producer(q):
    # 异步生产者函数，生成5个随机数作为项目，并放入异步队列中
    for _ in range(5):
        item = random.randint(1, 100)  # 随机生成1到100之间的数字
        await q.put(item)  # 异步将项目放入队列
        print(f"Produced item: {item}")  # 打印生产的项目
        await asyncio.sleep(random.random())  # 异步随机延迟以模拟生产时间


async def async_consumer(q):
    # 异步消费者函数，从异步队列中取出项目进行处理
    while True:
        item = await q.get()  # 异步从队列中取出一个项目
        if item is None:
            break  # 如果取到None则退出循环
        print(f"Consumed item: {item}")  # 打印消费的项目
        await asyncio.sleep(random.random())  # 异步随机延迟以模拟处理时间
    await q.task_done()  # 异步告诉队列此任务已完成


if __name__ == "__main__":
    # 同步部分
    producer_thread = threading.Thread(target=producer)  # 创建生产者线程
    consumer_thread = threading.Thread(target=consumer)  # 创建消费者线程

    producer_thread.start()  # 开始生产者线程
    consumer_thread.start()  # 开始消费者线程

    producer_thread.join()  # 等待生产者线程完成
    shared_queue.put(None)  # 发送结束信号给消费者
    consumer_thread.join()  # 等待消费者线程完成

    print("\nStarting async example...\n")  # 打印开始异步示例信息

    # 异步部分
    q = asyncio.Queue()  # 创建异步队列
    producer_task = asyncio.create_task(async_producer(q))  # 创建异步生产者任务
    consumer_task = asyncio.create_task(async_consumer(q))  # 创建异步消费者任务

    asyncio.run(producer_task)  # 运行异步生产者任务
    asyncio.run(consumer_task)  # 运行异步消费者任务

    print("Both producer and consumer have finished.")  # 打印生产者和消费者已完成的信息