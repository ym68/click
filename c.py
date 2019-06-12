# -*- coding: utf-8 -*-


'''

mouse auto click
mzg
2019.1.20

'''


import win32api, win32con, win32gui  

from datetime import datetime, date, time, timedelta
import time


def click():
    x,y=win32gui.GetCursorPos()

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

strnext_time = input('请输入开始点击时间，注意输入法切换为英文，如2019-01-19 23:28:00。:') 	
period = int(input('请输入再下一次自动点击时间间隔，如60 秒。 单位为秒：'))
print('下一次开始点击时间为 ',strnext_time,'再下一次自动点击时间间隔为 ',period,'秒')

if __name__ == '__main__':
    while True:
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):  
            i=1
            while i<2:
                i+=1
                click()
                time.sleep(0.2)  #每秒点击5次， 点击1次
            iter_time = iter_now + timedelta(seconds=period)
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print(strnext_time)
            continue

            
