"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 有趣的练习.py
@Author : 夏目&青一
@Time : 2022/11/16 20:44

"""
n = int(input('输入 一个数字>>>'))
i = 2

flag = True
while i <= n - 1:
    if n % i == 0:
        flag = False
    i +=1



if flag:
    print('是素数')
else:
    print('不是素数')

