import requests

url = ''
res = requests.get(url).content
print(res)
