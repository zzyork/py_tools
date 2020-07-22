import urllib.request
import http.cookiejar
import json
import os


url = "http://www.dmoe.cc/random.php?return=json"


def get_pic_url(url):
    response = urllib.request.urlopen(url)
    pic_url = json.loads(response.read())["imgurl"]
    # print(pic_url)
    return pic_url


def download_img(pic_url):
    pic_url = get_pic_url(url)
    request = urllib.request.Request(pic_url)
    try:
        img_name = "img.png"
        response = urllib.request.urlopen(request)
        filename = "D:\\personal\\Desktop\\编程\\python-scripts\\img\\" + img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"
# 

if __name__ == '__main__':
    download_img(url)
