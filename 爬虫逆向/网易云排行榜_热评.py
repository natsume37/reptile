"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 网易云排行榜_热评.py
@Author : 夏目&青一
@Time : 2022/11/2 17:40

"""
import requests

url = 'https://interface.music.163.com/weapi/v6/playlist/detail'

header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
    'referer': 'https://y.music.163.com/',
    'cookie': '_ntes_nnid=c23e9b446e5adc72f2176d0463ad27b9,1667381587830; _ntes_nuid=c23e9b446e5adc72f2176d0463ad27b9; NMTID=00OE6FaqDTT7aPZL0OovFzcgDJ6IaEAAAGEN6_uXg; WNMCID=atjlit.1667381588141.01.0; WEVNSM=1.0.0; JSESSIONID-WYYY=8wGskKuSg4r2kof79yAb1J7oJrDK%2FYwwOo%2FhEOspmnRynbhc%2FjpEhImYETeZl95umUD8xw9SOiu%5CGIN2r23hFAzUgnX%5CMxN%2Bt%2BvOXZ%2FBGSJ60%5Co%2BePgzbz4x5lNaqya38Ym2MFHCWtgUBGH6zNE5qv0d5UeD%2BYPgxO72emmDjXqWKNG0%3A1667383413271; _iuqxldmzr_=33'
}
parsel = 'params=BdxCXxNbKSpWc%2FZjoOetiee84Ke0nMDxNdAReDC4%2F5z4r85gRXuJsSBho3zeg%2BL%2BnW6RLK02KgWTxeenBZ5vLcbwPfy1V7HoZCPeDUJOmxs%3D&encSecKey=706880ece525b5227091a1ef6e86e0dcc26f753ea0b7eda66cb794b158cc7b0e069ad51d159a79d65491293db7e29697caa2a60db6169c8fc2ba5aa89743b3d9385a6205e30903ae0848d0e10594363189074de88a19448f5870740a0e0e31c60e37d157f3869cdf2dc7963aa304e3cf8781061217f5453cbfe3f62a46dfb208'
red = requests.post(url, headers=header, params=parsel)
# print(re.text)
res = red.json()
# html = res['privileges']
# res = red.text
# tag = re.findall(r'从此一个人',res)
print(type(res))
html = res['playlist']['tracks']
# print(html)
count = 1
for i in html:
    tag = i['name']
    print(f'第{count}:名  {tag}')
    count += 1
# 'Request URL: https://spa6.scrape.center/api/movie/?limit=10&offset=0&token=ZjY2MzcwYmFjNjBjNmNkYjMzY2M4YmFmYzkxMzRhOTM1Y2MwODQ2MiwxNjY3MzkzMTAz'
# 'Request URL: https://spa6.scrape.center/api/movie/?limit=10&offset=0&token=YTAyOGQ2ZTJhYTU2NDk0OGEzNDA5YjliNzg1ZjhlNzc2ODEyOTdjMywxNjY3MzkzMTk4'
# 'Request URL: https://spa6.scrape.center/api/movie/?limit=10&offset=0&token=ZjY2MzcwYmFjNjBjNmNkYjMzY2M4YmFmYzkxMzRhOTM1Y2MwODQ2MiwxNjY3MzkzMTAz'
