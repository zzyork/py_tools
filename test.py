import urllib.request,json,jsonpath

url = "http://api.tianapi.com/txapi/gjmj/index"
param = {"key":"2792e29b0ba6f08c4bfd7a8f188256c8"}
param = urllib.parse.urlencode(param)

url = "?".join([url,param])

response = str(json.loads(urllib.request.urlopen(url).read().decode("utf8"))["newslist"])
sentence = (response.strip("[")).strip("]")
sentence = json.loads(sentence)["content"]
print(sentence)