"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : re_bs4_豆瓣.py
@Author : 夏目&青一
@Time : 2022/10/27 13:50

"""
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.51 Safari/537.36 '
}
re = requests.get(url, headers=header)
html = BeautifulSoup(re.text, "html.parser")
list_works = html.select('#content > div > div.article > ol > li')
for i in list_works:
    tag = i.find('a')

    link = tag['href']
    name = tag.find('img')['alt']
    print(link,name)
    print()