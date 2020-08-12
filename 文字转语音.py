from aip import AipSpeech
import requests

APP_ID = '17905669'
API_KEY = 'xOoSYcRmhtEz2xzIG2utkjO0'
SECRET_KEY = 'Nx6x7SL6dx9Zf9PIzQyLun4CvLyPnE5Q '


def get_msg():
    url = 'http://open.iciba.com/dsapi/'   # 金山词霸每日一句 api 链接
    html = requests.get(url)
    content = html.json()['content']   # 获取每日一句英文语句
    note = html.json()['note']   # 获取每日一句英文的翻译语句
    return content, note

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 中文：zh 粤语：ct 英文：en

content, note = get_msg()
print(content)
print(note)

result = client.synthesis(note, 'zh', 1, {
    'vol': 5, 'per': 4, 'pit' : 7
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
