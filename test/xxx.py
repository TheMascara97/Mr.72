import threading
import queue
import time

# 创建一个队列
task_queue = queue.Queue()

# 工作线程类
class WorkerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # 从队列中获取任务
            task_data = self.queue.get()
            if task_data is None:
                # 如果是 None，就退出循环
                break
            print(f"线程 {self.name} 正在处理任务，数据为：{task_data}")
            # 模拟任务处理时间
            time.sleep(1)
            # 任务完成，向队列发送完成信号
            self.queue.task_done()

# 添加任务到队列
def add_task(data):
    task_queue.put(data)

# 同步函数，等待所有任务完成
def wait_all_tasks_done():
    task_queue.join()

# 主函数
if __name__ == "__main__":
    # 创建多个工作线程
    num_worker_threads = 3
    threads = []
    for i in range(num_worker_threads):
        worker = WorkerThread(task_queue)
        worker.start()
        threads.append(worker)

    # 添加一些任务到队列
    for i in range(10):
        add_task(f"任务 {i}")

    # 等待所有任务完成
    wait_all_tasks_done()

    # 停止工作线程
    for i in range(num_worker_threads):
        task_queue.put(None)
    for worker in threads:
        worker.join()

    print("所有任务已完成，线程已退出。")