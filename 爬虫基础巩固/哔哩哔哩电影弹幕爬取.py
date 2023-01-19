"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 哔哩哔哩电影弹幕爬取.py
@Author : 夏目&青一
@Time : 2022/10/27 16:02

"""


import requests
import json
import re


url = 'https://api.bilibili.com/x/v2/reply/main?callback=jQuery17207313619059537773_1666948899014&jsonp=jsonp&next=10&type=1&oid=31270285&mode=3&plat=1&_=1666949756368'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # ':authority': 'api.bilibili.com',
    'referer': 'https://www.bilibili.com/bangumi/play/ss25568?theme=movie&from_spmid=666.7.operation.2'
}
re = requests.get(url,headers=header)
# print(re.text)
print(type(re))
print(re.text)
res = json.dumps(re.text)

# jsons = json.loads(re.text)
# print(jsons)