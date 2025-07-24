import time
import schedule
from pywifi import PyWiFi, const, Profile
import speedtest_test
# 定义连接WIFI的函数
def connect_to_wifi(ssid, password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # 获取第一个无线网卡接口
    iface.disconnect()  # 断开当前连接
    time.sleep(1)  # 等待1秒
    if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        profile = Profile()
        profile.ssid = ssid  # 设置WIFI名称
        profile.auth = const.AUTH_ALG_OPEN  # 设置认证算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 设置密钥管理类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 设置加密类型
        profile.key = password  # 设置WIFI密码
        iface.remove_all_network_profiles()  # 移除所有网络配置文件
        tmp_profile = iface.add_network_profile(profile)  # 添加新的网络配置文件
        iface.connect(tmp_profile)  # 连接到指定WIFI
        time.sleep(10)  # 等待10秒，确保连接成功
        if iface.status() == const.IFACE_CONNECTED:
            with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
                file.write(f"Connected to {ssid}\n")
            print(f"Connected to {ssid}")
        else:
            with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
                file.write(f"Failed to connect to {ssid}\n")
            print(f"Failed to connect to {ssid}")

# 定义断开WIFI的函数
def disconnect_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # 获取第一个无线网卡接口
    iface.disconnect()  # 断开当前连接
    time.sleep(1)  # 等待1秒
    if iface.status() == const.IFACE_DISCONNECTED:
        with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
            file.write(f"Disconnected from WiFi\n")
    else:
        with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
            file.write(f"Failed to disconnect from WiFi\n")
# 定义定时任务
# def job():
#     print("Connecting to WiFi...")
#     connect_to_wifi("Atticus_test", "12345678")  # 替换为你的WIFI名称和密码
#     time.sleep(300)  # 保持连接5分钟
#     print("Disconnecting from WiFi...")
#     disconnect_wifi()

# # 设置定时任务，每小时运行一次
# schedule.every(1).minutes.do(job)

# # 主循环，运行定时任务
# while True:
#     schedule.run_pending()
#     time.sleep(1)
if __name__ == "__main__":
    i=0
    while i<30:
        i+=1
        with open(f'F:/code/speedtest_result', 'a', encoding="utf-8") as file:
            file.write(f"第 {i} 次测试开始\n")
        connect_to_wifi("Atticus", "12345678")  # 替换为你的WIFI名称和密码
        time.sleep(30) 
        speedtest_test.run_speedtest()
        time.sleep(300)  # 保持连接5分钟
        disconnect_wifi()
        time.sleep(1800)  # 断开连接20分钟



        