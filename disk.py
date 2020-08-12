#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 17:16
# @Author  : opsonly
# @Site    : 
# @File    : systemissue.py
# @Software: PyCharm

import psutil


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
    print('%.2f' % diskbaifen + "%")
disk()