import serial  
import time  
from datetime import datetime
import requests
import subprocess
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d') 

serial_port = 'com38'  # 根据实际情况修改串口名称，例如 Windows 上可能是 'COM3'  
baud_rate = 115200  # 根据实际情况修改波特率  
i=1  
# 打开串口  
ser = serial.Serial(serial_port, baud_rate, timeout=1)  
  
def read_and_judge(): 
    ser.close( )
    ser.open()



# while True:
#         try:
            
#             while True:  
                
#                 if ser.in_waiting > 0:  # 判断是否有数据可读  
                    
#                     data = ser.readline().decode('utf-8').strip()  # 读取一行数据并解码为字符串，去除换行符和空格  
#                     print(f"{data}")  
#                     with open(f'F:/code/sensor noderesult.txt', 'a', encoding="utf-8") as file: 

#                             file.write(f"{timestamp} {data})\n")
    
#                     # 根据接收到的数据进行判断  
#                     if "Fireware version:cdz-1.0.8-eng-f666246" in data:  
#                         print("升级成功cdz-1.0.8-eng-f666246'") 
#                         i+=1
#                         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#                         with open(f'F:/code/sensor noderesult.txt', 'a', encoding="utf-8") as file: 
#                             file.write(f"{timestamp} 第 {i} 次升级成功,当前版本cdz-1.0.5-eng-313aa4d\n")    
#         except Exception as e:  

#             print(f"An error occurred: {e}")

if__name__ == '__main__':

    serial_port = 'com38'  # 根据实际情况修改串口名称，例如 Windows 上可能是 'COM3'  
    baud_rate = 115200  # 根据实际情况修改波特率  
    
    # 打开串口  
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  
    data = ser.readline().decode('utf-8').strip()  # 读取一行数据并解码为字符串，去除换行符和空格  
    print(f"{data}")