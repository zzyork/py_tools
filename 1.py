import urllib.request,json

shici_url = "https://v1.jinrishici.com/all.json" #获取诗词名句、名字、作者、类型信息
response = urllib.request.urlopen(shici_url).read().decode("utf8")
sentence = json.loads(response)["content"]

print(type(response))