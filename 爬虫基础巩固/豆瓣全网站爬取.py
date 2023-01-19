"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 豆瓣全网站爬取.py
@Author : 夏目&青一
@Time : 2022/10/27 14:03

"""
import requests
from bs4 import BeautifulSoup
import time


def payi(url, n):
    url = f'https://movie.douban.com/top250?start={n}&filter='
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.51 Safari/537.36 '
    }
    re = requests.get(url, headers=header)
    html = BeautifulSoup(re.text, "html.parser")
    list_works = html.select('#content > div > div.article > ol > li')
    for i in list_works:
        global count
        tag = i.find('a')
        link = tag['href']
        name = tag.find('img')['alt']
        count += 1
        print(link, name)
        print()


start = time.time()
count = 0
for n in range(11):
    url = f'https://movie.douban.com/top250?start={n}&filter='
    payi(url, n)
low = time.time()
print(count)
print(f'程序耗时 {low - start}')
