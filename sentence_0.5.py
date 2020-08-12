import urllib.request
import json
import string
from urllib.parse import quote
import tkinter

def get_sentence(url): #定义函数获取句子
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("utf8"))["data"]
    sentence = json.loads(response.read().decode("utf8"))
    return sentence

def fun():
    text = get_sentence(url)
    data = tkinter.Label(garbage, text = text, justify = 'left').pack( side = 'left')
    return data

# 定义UI界面
garbage = tkinter.Tk()
garbage.title('垃圾分类') #UI框标题
garbage.geometry('200x200')
garbage.resizable()
entry = tkinter.Entry()
entry.pack()


gb_name = entry.get()
botton = tkinter.Button(garbage, text='确认').pack()


garbage.mainloop()
url_head = "https://api.66mz8.com/api/garbage.php?name="
url = quote(url_head + gb_name, safe=string.printable)
