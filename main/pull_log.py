import subprocess
import timestamp
from datetime import datetime
import time

def pull_log():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
# 定义要在cmd中执行的命令
    command = ['cmd', '/c', f'adb pull  /var/volatile/log/yocto.log {timestamp}.log']

# 启动进程
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 读取输出
    stdout, stderr = process.communicate()
    return_code = process.returncode

# 打印命令输出
    
    if return_code==1:

        return 1
    else:
        return 0

#pull_log()