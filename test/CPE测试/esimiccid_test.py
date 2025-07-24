import socket

import socket  
import time
from datetime import datetime
  
class UDPClient:  
    def __init__(self, broadcast_ip='192.168.1.1', port=9035, timeout=60, retries=3, delay=1):  
        self.broadcast_ip = broadcast_ip  
        self.port = port  
        self.server_address = (self.broadcast_ip, self.port)  
        self.timeout = timeout  # 设置超时时间  
        self.retries = retries  # 设置重试次数  
        self.delay = delay  # 设置重试之间的延迟时间  
  
        # 创建一个UDP套接字  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
        self.sock.settimeout(self.timeout)  # 设置套接字超时  
  
    def send(self, message, retries=None):  
        if retries is None:  
            retries = self.retries  
        if isinstance(message, str):  
            message = message.encode('utf-8')  
  
        try:  
            self.sock.sendto(message, self.server_address)  
            print(f"Message '{message.decode('utf-8')}' sent successfully.")  
        except socket.timeout:  
            if retries > 0:  
                print(f"Timeout occurred, retrying... ({retries} retries left)")  
                time.sleep(self.delay)  
                self.send(message, retries - 1)  
            else:  
                print(f"Failed to send message '{message.decode('utf-8')}' after {self.retries} retries.")  
        except Exception as e:  
            print(f"An error occurred: {e}")  
  
    def receive(self):  
        try:  
            data, _ = self.sock.recvfrom(1024)  # 缓冲大小为1024字节  
            return data.decode('utf-8')  
        except socket.timeout:  
            print("Receive timeout occurred.")  
            return None  
  
    def send_get(self, message):  
        self.send('get:' + message)  
  
    def send_set(self, message):  
        self.send('set:' + message)  

  
def get_iccid(slot,max_attempts = 3):
    for attempt in range(max_attempts):
        if slot == 1:
            client.send_get("esim1-iccid")
            response = client.receive()
        elif slot == 2:
            client.send_get("esim2-iccid")
            response = client.receive()
        else:
            return "none"
        print("raw iccid data ",response)
        if response is None:
            print(f"第{attempt + 1}次: 接收响应失败，重试...")
            continue
        data_arr  = response.split(':')
        if len(data_arr)>1  and "iccid" in str(data_arr[0]):
            iccid_str = str(data_arr[1])
            return iccid_str.strip(b'\x00'.decode())
        print(f"第{attempt + 1}次: 重试...")
    return "0000"

def get_esim(slot, max_attempts=3):
    for attempt in range(max_attempts):
        if slot == 1:
            client.send_get("esim1")
            response = client.receive()
        elif slot == 2:
            client.send_get("esim2")
            response = client.receive()
        else:
            return "none"
        if response is None:
            print(f"第{attempt + 1}次: 接收响应失败，重试...")
            continue
        print(response)
        if "success" in response:
            return True
        print(f"第{attempt + 1}次: 重试...")

    return False

def clear_etc(max_attempts = 3):
    for attempt in range(max_attempts):
        client.send_set("clear_fac")
        response = client.receive()
        if response is None:
            print(f"第{attempt + 1}次: 接收响应失败，重试...")
            continue
        if "success" in response:
            print("清除完成" ,response)
            return True
        
def restore_fac(max_attempts = 3):
    for attempt in range(max_attempts):
        client.send_set("restore_fac")
        response = client.receive()
        if response is None:
            print(f"第{attempt + 1}次: 接收响应失败，重试...")
            continue
        if "success" in response:
            print("恢复出厂设置成功" ,response)
            return True
               

if __name__ == "__main__":
    
    test_iccid1 = "89861122221039571579"
    test_iccid2 = "89861122221039571587"
    test_cnt = 0
    while True:
        client = UDPClient()
        test_cnt += 1  # Increment the test counter
        # 模拟半成品测试处的esim写入
        if get_esim(1) == 1:
            print("切换esim1成功 设备存储完成esim1 iccid")
            
        if get_esim(2) == 1:
            print("切换esim2成功 设备存储完成esim2 iccid")
        
        # 模拟整机测试的esim读出
            
        time.sleep(5)
        iccid1 = get_iccid(1)
        iccid2 = get_iccid(2)

        
        print("esim1的iccid",iccid1,test_iccid1)
        print("esim2的iccid",iccid2,test_iccid2)
        

        # 比较ICCID
        if iccid1 == test_iccid1:
            iccid1_flag = 1
            print("iccid1写入成功")
        else:
            iccid1_flag = 0
            print("iccid1写入失败")

        if iccid2 == test_iccid2:
            iccid2_flag = 1
            print("iccid2写入成功")
        else:
            iccid2_flag = 0
            print("iccid2写入失败")
        
        clear_etc()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        year = datetime.now().strftime('%Y')
        month = datetime.now().strftime('%m')
        day = datetime.now().strftime('%d')

       
    
        # Log the result to the file
        with open(f'F:/code/ICCID_log/{year}{month}{day}_result', 'a', encoding="utf-8") as file:  # 'a' mode appends to the file
            if iccid1_flag == 1 and iccid2_flag == 1:
                file.write(f"{timestamp} 第 {test_cnt} 次测试成功 {iccid1} {iccid2}\n")
            else:
                file.write(f"{timestamp} 第 {test_cnt} 次测试失败 失败原因 iccid1_flag: {iccid1_flag} iccid2_flag: {iccid2_flag}\n")
        
        restore_fac()
        time.sleep(60)  # Wait for 5 seconds before the next iteration