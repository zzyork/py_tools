import urllib.request
import http.cookiejar
import json
import os
from urllib.parse import quote
import string
import pathlib

url = quote("https://api.66mz8.com/api/rand.tbimg.php?format=json", safe=string.printable)

def get_pic_url(url):
    response = urllib.request.urlopen(url)
    pic_url = json.loads(response.read())["pic_url"]
    # print(pic_url)
    return pic_url

def download_img(pic_url):
    num = int(input("要多少自己输，多了小心电脑卡死："))
    num = num + 1
    path = os.path.expandvars('.\\udw_img')
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        print('{0} creat successful!'.format(path))
    else:
        print('{0} has been exists.'.format(path))
    
    for i in range(1, num):
        pic_url = get_pic_url(url)
        request = urllib.request.Request(pic_url)
        img_name = "img" + str(i) + ".jpg"
        try:
            response = urllib.request.urlopen(request)
            filename = ".\\udw_img\\" + img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())
                print("正在保存第" + str(i) + "张")
        except:
            pic_url = get_pic_url(url)
            request = urllib.request.Request(pic_url)
            response = urllib.request.urlopen(request)
            filename = ".\\udw_img\\" + img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())
                print("正在保存第" + str(i) + "张")

if __name__ == '__main__':
    download_img(url)
