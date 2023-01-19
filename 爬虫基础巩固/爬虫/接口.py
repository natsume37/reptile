import requests

url = 'http://www.wpsseo.cn/'

# 解析源
req = requests.get(url)
# 解码防止乱码
# print(re.content.decode('utf-8'))
req.encoding = req.apparent_encoding
reqs = req.text
print(reqs)
