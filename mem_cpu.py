#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 17:16
# @Author  : opsonly
# @Site    : 
# @File    : systemissue.py
# @Software: PyCharm

import psutil

def memory():
    print('内存信息：')
    mem = psutil.virtual_memory()
    # 单位换算为MB
    memtotal = mem.total/1024/1024
    memused = mem.used/1024/1024
    membaifen = mem.percent

    print('已用内存：\t\t%.2fMB' % memused)
    print('总内存：\t\t%.2fMB' % memtotal)

def disk():
    print('磁盘信息：')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    #单位换算为GB
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = diskuse.total / 1024 / 1024 / 1024
    diskbaifen = diskused / disktotal * 100
    print('%.2fGB' % diskused)
    print('%.2fGB' % disktotal)
    print('%.2f' % disk.percent + "%")


memory()
print('*******************')
disk()

