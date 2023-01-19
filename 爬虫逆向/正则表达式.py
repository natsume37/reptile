"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 正则表达式.py
@Author : 夏目&青一
@Time : 2022/11/2 16:19

"""
import re

h = '这是一个文本 16-608855782这是一个电话'

tex =re.findall(r'(?:1\d{2})(?:\d{8})',h)
print(tex)
t = re.search(r'(\d{2})-(\d{3})',h)
print(t.group(2))


