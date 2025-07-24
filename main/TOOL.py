import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from SSH import SSH
import enable_ssh
import pull_log
import time
import get_ip
import subprocess
def on_button_click_one():
    enable_ssh.main_reset()

    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("150x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text="设备已恢复出厂设置")
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_two():
   
    enable_ssh.main_SSH()
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("150x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text="SSH已打开")
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_three():

    enable_ssh.main_ADB()
    #time.sleep(15)
    #enable_ssh.main_reboot()
    
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("150x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text="ADB已打开")
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_four():
    enable_ssh.main_ADB()
    result=pull_log.pull_log()
    
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("200x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    if result == 1:
        label = tk.Label(popup, text="log导出失败,未连接ADB")
        label.pack(pady=20)  # 添加外边距
    else:
    
        label = tk.Label(popup, text="log已导出")
        label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_five():
    enable_ssh.main_SSH()

    result=SSH().get_ICCID()
# 创建一个新窗口
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("内置卡ICCID")

# 设置窗口大小
    popup.geometry("200x200")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text=result)
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_six():
    enable_ssh.main_SSH()
    SSH().enter_fac()
   
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("150x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text="设备已进入产测模式")
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
def on_button_click_seven():
    enable_ssh.main_SSH()
    SSH().exit_fac()
   
    popup = tk.Toplevel()

# 设置窗口标题
    popup.title("提示")

# 设置窗口大小
    popup.geometry("150x100")  # 宽度x高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口宽度和高度
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # 计算窗口位置
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    popup.geometry(f"+{position_right}+{position_down}")

# 创建一个标签并添加文本
    label = tk.Label(popup, text="设备已退出产测模式")
    label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    button = tk.Button(popup, text="关闭", command=popup.destroy)
    button.pack()
# def on_button_click_eight():
#         # # console=subprocess.Popen(["start", "cmd"], shell=True)
#         # messages = ["Hello, World!", "This is a test message.", "Exiting..."]
#         # for message in messages:
#         #     console.stdin.write(message + "\n")
#         #     console.stdin.flush()  # 确保内容被写入
#         # time.sleep(1)
        
#         time.sleep(5)
#         enable_ssh.main_SSH()
        
#         SSH().tail_log_file()
        



        # def __init__(self, root):
        #     self.root = root
        #     self.root.title("打开控制台示例")

        # # 创建一个按钮，点击后打开控制台窗口
        #     self.button = tk.Button(root, text="打开控制台", command=self.open_console)
        #     self.button.pack(pady=20)

        # def open_console(self):
        # """打开一个新的控制台窗口"""
        # # 使用 subprocess 启动一个新的 cmd 窗口
        #     subprocess.Popen(["start", "cmd"], shell=True)
        #     print("控制台已打开")
        
   
    # popup = tk.Toplevel()

# # 设置窗口标题
#     popup.title("提示")

# # 设置窗口大小
#     popup.geometry("150x100")  # 宽度x高度
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     # 获取窗口宽度和高度
#     window_width = popup.winfo_reqwidth()
#     window_height = popup.winfo_reqheight()

#     # 计算窗口位置
#     position_right = int((screen_width - window_width) / 2)
#     position_down = int((screen_height - window_height) / 2)

    # 设置窗口位置
    # popup.geometry(f"+{position_right}+{position_down}")

# # 创建一个标签并添加文本
#     label = tk.Label(popup, text="")
#     label.pack(pady=20)  # 添加外边距

# 创建一个按钮，点击后关闭弹窗
    # button = tk.Button(popup, text="关闭", command=popup.destroy)
    # button.pack()


# def on_button_click_eight():
#     enable_ssh.main_SSH()
#     SSH().open_dump()
   
#     popup = tk.Toplevel()

# # 设置窗口标题
#     popup.title("提示")

# # 设置窗口大小
#     popup.geometry("150x100")  # 宽度x高度
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     # 获取窗口宽度和高度
#     window_width = popup.winfo_reqwidth()
#     window_height = popup.winfo_reqheight()

#     # 计算窗口位置
#     position_right = int((screen_width - window_width) / 2)
#     position_down = int((screen_height - window_height) / 2)

#     # 设置窗口位置
#     popup.geometry(f"+{position_right}+{position_down}")

# # 创建一个标签并添加文本
#     label = tk.Label(popup, text="dump已打开")
#     label.pack(pady=20)  # 添加外边距

# # 创建一个按钮，点击后关闭弹窗
#     button = tk.Button(popup, text="关闭", command=popup.destroy)
#     button.pack()


# def on_select():
#     # 当用户选择下拉框中的选项时，这个函数会被调用
#     all_ip=get_ip.desired_ip()
#     print(f"Selected item: {all_ip}")



def create_buttons(root):
    """
    创建并排列8个不同类型的按钮。

    参数:
    root (tk.Tk): Tkinter的主窗口对象,按钮将被创建并添加到这个窗口。

    返回:
    无。此函数直接修改传递的root参数的内容,不返回任何值。
    """
    # 定义不同类型的按钮属性
    # buttons = [
    #     {"text": "恢复出厂", "bg": "white", "command": lambda: on_button_click_one()},
    #     {"text": "打开SSH", "bg": "white", "command": lambda: on_button_click_two()},
    #     {"text": "打开ADB", "bg": "white", "command": lambda: on_button_click_three()},
    #     {"text": "导出log", "bg": "white", "command": lambda: on_button_click_four()},
    #     {"text": "获取ICCID", "bg": "white", "command": lambda: on_button_click_five()},
    #     {"text": "进入产测模式", "bg": "white", "command": lambda: on_button_click_six()}
    # ]
    
    btn1 = tk.Button(root, text="恢复出厂设置",command=lambda: on_button_click_one())
    btn1.grid(row=2, column=1, padx=5, pady=5)

    btn2 = tk.Button(root, text="打开SSH", command=lambda: on_button_click_two())
    btn2.grid(row=0, column=0, padx=5, pady=5)
    btn3 = tk.Button(root, text="打开ADB", command=lambda: on_button_click_three())
    btn3.grid(row=0, column=1, padx=5, pady=5)
    btn4 = tk.Button(root, text="导出log", command=lambda: on_button_click_four())
    btn4.grid(row=3, column=0, padx=10, pady=10)
    btn5 = tk.Button(root, text="获取ICCID", command=lambda: on_button_click_five())
    btn5.grid(row=0, column=2, padx=10, pady=10)
    btn6 = tk.Button(root, text="进入产测模式", command=lambda: on_button_click_six())
    btn6.grid(row=3, column=1, padx=10, pady=10)
    btn7 = tk.Button(root, text="退出产测模式", command=lambda: on_button_click_seven())
    btn7.grid(row=3, column=2, padx=5, pady=5)
    # btn8 = tk.Button(root, text="打印log", command=lambda: on_button_click_eight())
    # btn8.grid(row=2, column=2, padx=5, pady=5)
    # btn8 = tk.Button(root, text="打开dump", command=lambda: on_button_click_eight())

    
# def main():
#     root = tk.Tk()
#     root.title("下拉框示例")

#     # 创建下拉框
#     combo = ttk.Combobox(root)
#     combo['values'] = ('选项1', '选项2', '选项3', '选项4', '选项5')
#     combo.bind("<<ComboboxSelected>>", on_select)
#     combo.pack(pady=10)

#     root.mainloop() 
#     # # 创建并排列按钮
#     # for button_config in buttons:
#     #     button = tk.Button(root, **button_config)
#     #     button.pack(pady=10)

# 主程序入口
if __name__ == "__main__":
    
    # 创建主窗口
    root = tk.Tk()
    # 设置窗口标题
    root.title("快捷按键")
    window_width = 300  # 你可以根据需要设置窗口大小
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_right = int((screen_width - window_width) / 2)
    position_down = int((screen_height - window_height) / 2)

    # 设置主窗口位置和大小
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    # 调用函数创建按钮
    create_buttons(root)
    

    # 进入消息循环
    root.mainloop()
    