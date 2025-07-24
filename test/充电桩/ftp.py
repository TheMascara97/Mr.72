import ftplib
import serial
import time

def ftp_connect():
    ftp_host = "8.137.116.71"
    ftp_port = 10021
    ftp_user = "otaUser"
    ftp_password = "ota123456"

    try:
        # 连接到 FTP 服务器
        ftp = ftplib.FTP()
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_password)
        print(f"Connected to FTP server {ftp_host}:{ftp_port} as user {ftp_user}")
        return ftp
    except ftplib.all_errors as e:
        print(f"Error connecting to FTP server: {e}")
        return None
def ftp_upload1():
    ftp = ftp_connect()
    if ftp is not None:
        # 上传文件
        local_file_path = "F:/智行充电桩/cdz-1.0.5-eng-313aa4d/cdz_app.bin"  # 本地文件路径
        remote_file_path = "/cdz_app.bin"  # 远程文件路径
        
        with open(local_file_path, "rb") as file:
            ftp.storbinary(f'STOR {remote_file_path}', file)  
            print(f"File {local_file_path} uploaded successfully to {remote_file_path}")
    # ftp.quit()


def ftp_upload2():
    ftp = ftp_connect()
    if ftp is not None:
        # 上传文件
        local_file_path = "F:/智行充电桩/cdz-1.0.5-eng-313aa4d/cdz_app.bin"  # 本地文件路径
        remote_file_path = "/cdz_app.bin"  # 远程文件路径

        with open(local_file_path, "rb") as file:
            ftp.storbinary(f'STOR {remote_file_path}', file) 
            print(f"File {local_file_path} uploaded successfully to {remote_file_path}")
    # 在这里可以进行其他 FTP 操作
    # 例如，上传文件、下载文件、列出目录等
    # 操作完成后，记得关闭 FTP 连接
    ftp.quit()
#ftp_connect()
# ftp_upload1()