import urllib.request
import http.cookiejar
import json
import os
from urllib.parse import quote
import string

url = quote("https://api.66mz8.com/api/rand.tbimg.php?format=json", safe=string.printable)

# print (url)


def get_pic_url(url):
    response = urllib.request.urlopen(url)
    pic_url = json.loads(response.read())["pic_url"]
    # print(pic_url)
    return pic_url


def download_img(pic_url):
    for i in range(1,51):
        pic_url = get_pic_url(url)
        request = urllib.request.Request(pic_url)
        img_name = "img" + str(i) + ".jpg"
#         print (img_name)
        try:
            response = urllib.request.urlopen(request)
            filename = "D:\\personal\\Desktop\\编程\\python-scripts\\udw_img\\" + img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())  # 将内容写入图片
        except:
            pic_url = get_pic_url(url)
            request = urllib.request.Request(pic_url)
            response = urllib.request.urlopen(request)
            filename = "D:\\personal\\Desktop\\编程\\python-scripts\\udw_img\\" + img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())  # 将内容写入图片


if __name__ == '__main__':
    download_img(url)
