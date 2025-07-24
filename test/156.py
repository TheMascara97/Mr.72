from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

def task():
    print("任务执行了！")

# 创建调度器
scheduler = BlockingScheduler()

# 指定目标时间（例如：明天的 10:30）
target_time = datetime.now().replace(hour=11, minute=18, second=0, microsecond=0) + timedelta(days=0)

# 添加任务
scheduler.add_job(task, 'date', run_date=target_time)

# 启动调度器
scheduler.start()