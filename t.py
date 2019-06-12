# -*- coding: utf-8 -*-



import requests
import datetime
import time
import os
import ntplib
from time import ctime


# host = 'http://crm.schtrust.com/activeDesktop2.jsp'

# host = 'https://www.baidu.com'
# host = 'https://www.12306.cn'
host = 'https://www.taobao.com'



def get_webservertime(host):
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'} 
    r = requests.get(host, headers = headers)

    tss=  r.headers['Date'] #获取http头date部分 string
    # print(ts)
              
    # 提取GMT时间的字符串
    tsp = time.strptime(tss[5:25], "%d %b %Y %H:%M:%S")  # string to time tuple
    ts = time.mktime(tsp) 
    tsn = ts + 8*60*60 + 0.86  # timestamp + Beijing time + time delay , then to time tuple
    tsnp = time.localtime(tsn) #timestamp to local time tuple
    # print (tsnp)

    dat="Date %u-%02u-%02u"%(tsnp.tm_year,tsnp.tm_mon,tsnp.tm_mday)
    tm="Time %02u:%02u:%02u"%(tsnp.tm_hour,tsnp.tm_min,tsnp.tm_sec)
    print ('服务器端',host,'的系统时间是',dat,tm)
    

    c = ntplib.NTPClient() #创建一个NTPClient的实例
    s = c.request('ntp5.aliyun.com') #通过对象的request方法得到NTPStats的对象
    current_time = s.tx_time # time stamp
    _date, _time = str(datetime.datetime.fromtimestamp(current_time))[:23].split(' ')
    # print("北京标准时间  ", str(datetime.datetime.fromtimestamp(current_time))[:23])

    dif_time = round((current_time - ts - 8*60*60 ),3)
    
    
    m, s = divmod(dif_time, 60)
    h, m = divmod(m, 60)

    # print('服务器端时间比北京标准时间慢：', dif_time,'秒')
    print('服务器端时间比北京标准时间慢：',int(m),'分', s,'秒')

    print ('北京标准时间   ', _date, _time)

    # print(tsnp)
    
    print ('本机同步前时间 ', str(datetime.datetime.now())[:23])  #.003, 毫秒级

    os.system(dat)
    os.system(tm)

 
    print ('本机同步后时间 ', str(datetime.datetime.now())[:23])


    
get_webservertime(host) #同步服务器端时间




