import urllib.request,json,os,string,datetime
from tkinter import Label,Tk,Button,PhotoImage
from PIL import ImageFont,Image,ImageDraw
from urllib.parse import quote
from multiprocessing import Process,Value,Lock

def get_pic_url(url):
    response = urllib.request.urlopen(url)
    pic_url = json.loads(response.read())["pic_url"]
    return pic_url

def down_img():
    pic_url = quote("https://s1.ax1x.com/2020/07/29/aebhcj.jpg", safe=string.printable)
    request = urllib.request.Request(pic_url)
    response = urllib.request.urlopen(request)
    filename = "bg_img.jpg"
    if (response.getcode() == 200):
        with open(filename, "wb") as f:
            f.write(response.read())

def sentence():
    shici_url = "https://v1.jinrishici.com/all.json" #获取诗词名句、名字、作者、类型信息
    response = urllib.request.urlopen(shici_url).read().decode("utf8")
    sentence = json.loads(response)["content"]
    strs = Value(str, sentence)
    return sentence,strs

def img():
    p1 = Process(target=sentence)
    p1.start()
    p1.join()
    p2 = Process(target=down_img)
    p2.start()
    p2.join()
    imageFile = "bg_img.jpg"
    file_save_dir = ".\\"
    #初始化参数
    x = 150
    y = 75
    font = ImageFont.truetype("C:\\Windows\\Fonts\\simkai.ttf",50)
    im1=Image.open(imageFile)
    draw = ImageDraw.Draw(im1)
    right = 0   #往右位移量
    down = 0    #往下位移量
    w = 500     #文字宽度（默认值）
    h = 500     #文字高度（默认值）
    row_hight = 5 #行高设置（文字行距）
    word_dir = 0 #文字间距
    for k,s2 in enumerate(strs):
        if k == 0:
            w,h = font.getsize(s2)
        # if s2 == "\n" or s2 == "。" or s2 == "、" or s2 == "！" or s2 == "？" :
        if s2 == "," or s2 == "\n" or s2 == "，" or s2 == "。" or s2 == "、" or s2 == "！" or s2 == "？" :
            right = right - w - row_hight
            down = 0
            continue
        else :
            down = down+h + word_dir
        draw.text((x+right, y+down),s2,(100,100,100),font=font)
    # new_filename = file_save_dir +  strs.replace(",","-").replace("\n","-") + ".jpg"
    new_filename = file_save_dir + "shici.png"
    im1.save(new_filename)
    del draw
    im1.close()

def shici():
    start = datetime.datetime.now()
    print(start)
    img()
    shici = Tk()
    shici.title("今日诗词")
    img_png = PhotoImage(file = 'shici.png')
    label_img = Label(shici, image = img_png)
    label_img.pack()
    end = datetime.datetime.now()
    print(end)
    print( end - start )
    shici.mainloop()

def del_img():
    os.remove("bg_img.jpg")
    os.remove("shici.png")


if __name__ == '__main__':
    strs = "测试"
    shici()
    del_img()