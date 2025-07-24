import serial  
import time  

from datetime import datetime
import requests

import ftp


import ftplib
import serial
import time


# 配置串口参数  
serial_port = 'com30'  # 根据实际情况修改串口名称，例如 Windows 上可能是 'COM3'  
baud_rate = 115200  # 根据实际情况修改波特率  
  
# 打开串口  
ser = serial.Serial(serial_port, baud_rate, timeout=1)  
  
def read_and_judge(): 
    ser.close( )
    ser.open()
    

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d') 
    i=1
    while True:
        try:
            
            while True:  
                
                if ser.in_waiting > 0:  # 判断是否有数据可读  
                    
                    data = ser.readline().decode('utf-8').strip()  # 读取一行数据并解码为字符串，去除换行符和空格  
                    print(f"{data}")  
                    with open(f'F:/code/cdzfota_log/result.txt', 'a', encoding="utf-8") as file: 
                            file.write(f"{timestamp} {data})\n")
    
                    # 根据接收到的数据进行判断  
                    if "Fireware version:cdz-1.0.8-eng-f666246" in data:  
                        print("升级成功cdz-1.0.8-eng-f666246'") 
                        i+=1
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        with open(f'F:/code/cdzfota_log/result.txt', 'a', encoding="utf-8") as file: 
                            file.write(f"{timestamp} 第 {i} 次升级成功,当前版本cdz-1.0.5-eng-313aa4d\n")

                        # ftp.ftp_upload2()
                        time.sleep(30)
                        # HTTPS URL
                        url = 'https://www.yingmakj.com/mini/device/test/cmd/861337071182806?cmd=24'

                                # 发送GET请求
                        response = requests.get(url)

    # 检查请求是否成功
                        if response.status_code == 200:
        # 打印网页内容
                            print(response.text)
                        else:
                            print('请求失败，状态码：', response.status_code)
                        
                        


                    elif "cdz-1.0.8-eng-f666246" in data: 
                        i+=1
                        print("升级成功cdz-1.0.8-eng-f666246'") 
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        with open(f'F:/code/cdzfota_log/result.txt', 'a', encoding="utf-8") as file: 
                            file.write(f"{timestamp} 第 {i} 次升级成功,当前版本cdz-1.0.5-eng-313aa4d\n")
                        # ftp.ftp_upload1()
                        time.sleep(30)
                                            # HTTPS URL
                        url = 'https://www.yingmakj.com/mini/device/test/cmd/861337071182806?cmd=24'

                                # 发送GET请求
                        response = requests.get(url)

                                # 检查请求是否成功
                        if response.status_code == 200:
                                # 打印网页内容
                            print(response.text)
                        else:
                            print('请求失败，状态码：', response.status_code)
                    elif "read ota file failed" in data:
                        timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                        with open(f'F:/code/cdzfota_log/result.txt', 'a', encoding="utf-8") as file: 
                            file.write(f"{timestamp} 出现失败\n")   
                    # else:  
                    #     print(f"{data}")  
    
                # 休眠一段时间，避免读取频率过高  
                    # with open(f'F:/code/cdzfota_log/{year}{month}{day}_result.txt', 'a', encoding="utf-8") as file: 
                    #     if upgrade_result == 1:
                    #         file.write(f"{timestamp} 第 {i} 次升级成功\n")
                    #     if upgrade_result == 2:
                    #         file.write(f"{timestamp} 第 {i} 次升级成功\n")
                time.sleep(0.1)  
                
        except Exception as e:  

            print(f"An error occurred: {e}")
              
        finally:  
            ser.close()  
            ser.open()
            # ser = serial.Serial(serial_port, baud_rate, timeout=1)
            print("Serial port closed")  
  
if __name__ == "__main__":  
    read_and_judge()