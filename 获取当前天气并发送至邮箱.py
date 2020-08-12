#coding: utf-8    

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header
import requests

def get_weather():
    url = 'http://v.juhe.cn/weather/index?cityname=苏州&key=4ef373c97397656d4235c8e21f5d018a'  # 城市名cityname和key值换成自己的
    weather_json = requests.get(url).json()
    temperature = weather_json['result']['today']['temperature']
    weather = weather_json['result']['today']['weather']
    week = weather_json['result']['today']['week']
    city = weather_json['result']['today']['city']
    dressing_advice = weather_json['result']['today']['dressing_advice']
    return temperature, weather, week, city, dressing_advice
    
temperature, weather, week, city, dressing_advice = get_weather()
weather_msg = ('今天是：' + week + '\n' \
	  + city + '的天气：' + weather + '\n' \
	  + '今天温度：' + temperature +'\n' \
	  + '穿衣指南：' + dressing_advice)
print(weather_msg)




    
#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
username = 'zhangyuhao781@163.com'
password='zyh951209'
sender='zhangyuhao781@163.com'
#receiver='XXX@126.com'
#收件人为多个收件人
receiver=['1004921724@qq.com','211446947@qq.com']

subject = '今天的天气信息来咯！！'
#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
#subject = '中文标题'
#subject=Header(subject, 'utf-8').encode()
    
#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = 'Yorkzhang <XXX@163.com>'
#msg['To'] = 'XXX@126.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver) 
#msg['Date']='2012-3-16'

#构造文字内容
text = weather_msg
text_plain = MIMEText(text,'plain', 'utf-8')    
msg.attach(text_plain)

#构造图片链接
sendimagefile=open(r'D:\pythontest\testimage.png','rb').read()
image = MIMEImage(sendimagefile)
image.add_header('Content-ID','<image1>')
image["Content-Disposition"] = 'attachment; filename="testimage.png"'
msg.attach(image)

#发送邮件
smtp = smtplib.SMTP()    
smtp.connect('smtp.163.com')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()
