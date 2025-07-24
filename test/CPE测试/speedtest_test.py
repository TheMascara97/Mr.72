import speedtest
import schedule
import time
import csv
from datetime import datetime

# 定义测试函数
def run_speedtest():
    try:
        # 初始化 Speedtest 客户端
        st = speedtest.Speedtest()
        st.get_best_server()

        # 测试下载速度
        download_speed = st.download() / 10**6  # 转换为 Mbps
        # 测试上传速度
        upload_speed = st.upload() / 10**6  # 转换为 Mbps
        # 获取延迟
        ping = st.results.ping

        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 打印结果
        print(f"Time: {current_time}, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping:.2f} ms")

        # 将结果保存到 CSV 文件
        with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
            file.write(f"{current_time},{download_speed:.2f},{upload_speed:.2f},{ping:.2f}\n")

    except Exception as e:
        with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
            file.write(f"Error: {e}\n")

# 定义调度任务
# def job():
#     print("Running speedtest...")
#     run_speedtest()

# # 设置定时任务，每小时运行一次
# schedule.every(1).minutes.do(job)

# # 主循环
# while True:
#     schedule.run_pending()
#     time.sleep(1)