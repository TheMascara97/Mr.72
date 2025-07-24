#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
del_first5_dirs.py
删除 Windows 指定路径下的前 5 个文件夹（按名称升序）
用法：
    python del_first5_dirs.py "D:\Projects"
    python del_first5_dirs.py "C:\Temp" --yes
"""
import os
import sys
import shutil
from pathlib import Path

def del_first5_dirs(root: str, auto_confirm: bool = False):
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        print(f"路径不存在或不是目录: {root}")
        return

    # 只取一级子目录，并按名称排序
    dirs = sorted([d for d in root.iterdir() if d.is_dir()])[:5]
    if not dirs:
        print("目录下没有子文件夹，无需删除。")
        return

    print(f"\n即将删除以下 {len(dirs)} 个文件夹：")
    for d in dirs:
        print("  ", d)

    if not auto_confirm:
        choice = input("\n确认删除？(y/n): ").strip().lower()
        if choice != 'y':
            print("已取消操作。")
            return

    for d in dirs:
        try:
            shutil.rmtree(d)
            print(f"已删除: {d}")
        except Exception as e:
            print(f"删除失败: {d} ({e})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python del_first5_dirs.py <目录路径> [--yes]")
        print("示例: python del_first5_dirs.py \"C:\\Temp\" --yes")
        sys.exit(1)

    target = sys.argv[1]
    confirm_flag = "--yes" in sys.argv
    del_first5_dirs(target, auto_confirm=confirm_flag)
    # 追加到 del_first5_dirs.py 最下方
if __name__ == "__main__":
    import time

    TARGET   = "E:\\test\\"   # 改为你自己的路径
    INTERVAL = 3600                # 10 分钟 = 600 秒

    print("守护进程已启动，每 60 分钟执行一次删除，按 Ctrl+C 退出。")
    try:
        while True:
            del_first5_dirs(TARGET, auto_confirm=True)  # 跳过交互
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("用户终止。")