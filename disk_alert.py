#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import psutil
import socket
import dingtalkchatbot.chatbot as cb
import datetime
import re
import utils

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

hostname = socket.gethostname()

now_time = (datetime.datetime.now()).strftime("%Y-%m-%d")

mem = psutil.virtual_memory()
# 单位换算为MB
memtotal = float(mem.total / 1024 / 1024)
memused = float(mem.used / 1024 / 1024)
memper = mem.percent

disk = psutil.disk_partitions()
diskuse = psutil.disk_usage('/')
#单位换算为GB
diskused = float(diskuse.used / 1024 / 1024 / 1024)
disktotal = float(diskuse.total / 1024 / 1024 / 1024)
diskper = diskused / disktotal * 100

diskalert = "  事件：硬盘告警\n  告警主机：%s\n  IP地址：%s\n  当前硬盘使用率：%.1f%%\n  已使用硬盘大小：%.1fGB\n  硬盘总大小：%.1fGB\n  告警时间：%s \n" % (hostname, get_ip(), diskper, diskused, disktotal, now_time)
memalert = "  事件：内存告警\n  告警主机：%s\n  IP地址：%s\n  当前内存使用率：%.1f%%\n  已使用内存大小：%.1fMB\n  内存总大小：%.1fMB\n  告警时间：%s \n" % (hostname, get_ip(), memper, memused, memtotal, now_time)

def Es_dingding(webhook, domain):
    ding = cb.DingtalkChatbot(webhook)
    if int(diskper) > int("70"):
        ding.send_text(msg=diskalert)
    elif int(memper) > int("80"):
		ding.senf_text(msg=memalert)
    print(diskalert)
    print('*******************')
    print(memalert)
    return
    
#测试
Es_dingding('https://oapi.dingtalk.com/robot/send?access_token=06b756937449d2a96c91167e117973ab8b67819f8cc88081001df0ec382cac22', 'taozuang.com')
