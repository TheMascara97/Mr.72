import subprocess
from datetime import datetime
import time
import os
def ping_host():
# 定义要运行的命令
    ip_address = "www.qq.com"
    # command = "adb shell ping www.qq.com  -c3"
    if os.name == 'nt':  # Windows
        command = ['ping', '-n', '5', ip_address]
        with open(f'F:/code/1111.txt', 'a', encoding="utf-8") as file:
# # 创建子进程并捕获输出
            process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            for line in process.stdout:
                file.write(f"{line.strip()}\n")
    else:  # Linux and macOS
        command = ['ping', '-c', '1', ip_address]

    return subprocess.call(command) == 0



#            return line.strip()
#     time.sleep(5)





#时输出命令的执行结果
    # print("Standard Output:")
    # for line in process.stdout:
    #     print(line.strip())


    # 等待子进程结束
    process.wait()

    # # 输出标准错误内容（如果有）
    # stderr = process.stderr.read()
    # if stderr:
    #     print("Standard Error:")
    #     print(stderr)

    # # 输出返回码
    # print("Return Code:", process.returncode)
def reboot():
    command = "adb shell reboot"
    # 创建子进程并捕获输出
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
        )

# 实时输出命令的执行结果
    print("Standard Output:")
    for line in process.stdout:
        print(line.strip())

    # 等待子进程结束
    process.wait()

    # 输出标准错误内容（如果有）
    stderr = process.stderr.read()
    if stderr:
        print("Standard Error:")
        print(stderr)

    # 输出返回码
    print("Return Code:", process.returncode)


def main():
    
    i=0
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d') 
    while True:
        i+=1
        
        with open(f'F:/code/1111.txt', 'a', encoding="utf-8") as file:
            # file.write(f"{timestamp} 第{i}次测试\n")
            file.write(f"{timestamp}第{i}次测试\n")
        #ping_host()
        time.sleep(10)
        reboot()
        time.sleep(60)
if __name__ == "__main__":
    main()