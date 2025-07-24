import get_ip
import os
import enable_ssh
import get_ip
import subprocess
import time
import tkinter as tk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import time
import ctypes
import sys
import time



base_ip = f'{enable_ssh.process_string()}1'
class SSH:
    
    def __init__(self):
        import paramiko
        
        self.ssh = paramiko.SSHClient()
 
# 允许连接不在know_hosts文件中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        name=f'{base_ip}'
# 连接服务器
        self.ssh.connect(hostname=name, port=22, username='root', password='quectel')
    def get_infomation(self,code1,code2,code3):
       
        stdin, stdout, stderr = self.ssh.exec_command(code1)
        info1=stdout.read().decode('UTF-8')
        print(info1,end="")
        stdin, stdout, stderr = self.ssh.exec_command(code2)
        info2=stdout.read().decode('UTF-8')
        print(info2,end="")
        stdin, stdout, stderr = self.ssh.exec_command(code3)
        info3=stdout.read().decode('UTF-8')
        print(info3,end="")
    def get_ICCID(self):

            stdin, stdout, stderr = self.ssh.exec_command('cat /etc/productinfo/esim1_iccid')
            esim1=stdout.read().decode('UTF-8')
            stdin, stdout, stderr = self.ssh.exec_command('cat /etc/productinfo/esim2_iccid')
            esim2=stdout.read().decode('UTF-8')
            stdin, stdout, stderr = self.ssh.exec_command('cat /etc/productinfo/esim3_iccid')
            esim3=stdout.read().decode('UTF-8')

            result=str(esim1)+str(esim2)+str(esim3)
            # print(result,end="")
            if result !="":
                 return result
            else:
                 return "无内置卡"
                 
   

    import subprocess

    def tail_log_file(self):
        stdin, stdout, stderr = self.ssh.exec_command('tail -f /var/volatile/log/yocto.log')
        try:
            while True:
                # 按行读取输出
                line = stdout.readline()

                if not line:
                    break  # 如果没有输出，退出循环
                # return line.encode('utf-8').strip()
                print(line, end="")
                
        except KeyboardInterrupt:
            print("\n日志跟踪已中断。")
        finally:
            # 关闭通道
            stdout.channel.close()
            stderr.channel.close()

# 示例：跟踪日志文件

        
        
    def enter_fac(self):
        stdin, stdout, stderr = self.ssh.exec_command('rm /etc/productinfo/fac_done')
        
        stdin, stdout, stderr = self.ssh.exec_command('sync')
        stdin, stdout, stderr = self.ssh.exec_command('reboot')
        
        print("设备重启",end="")
    def exit_fac(self):
        stdin, stdout, stderr = self.ssh.exec_command('touch /etc/productinfo/fac_done')
        
        stdin, stdout, stderr = self.ssh.exec_command('sync')
        stdin, stdout, stderr = self.ssh.exec_command('reboot')
        
        print("设备重启",end="")



if __name__ == "__main__":
  
    SSH().tail_log_file()
