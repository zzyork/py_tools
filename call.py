# -*- coding: utf-8 -*-

import smtplib
import subprocess
import os
import re

di=subprocess.Popen(['docker','inspect','bc189bf219b2'], stdout=subprocess.PIPE)
print (di)
out,err=di.communicate()
#匹配容器运行状态
pattern='(\d*).*(Status).*'
docker_status=re.search(pattern,out)
docker_status_line=docker_status.group()
#替换多余的字符串
result=docker_status_line.replace(" ","").replace("\"","").replace(",","")