"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : study_gju.py
@Author : 夏目&青一
@Time : 2022/10/18 16:22

"""

import time

from selenium.webdriver import Chrome


web = Chrome()

web.get('https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=221258875&clazzid=60766047&cpi=217041836&enc=50ccbd39cc10c819d4c7458c416806f0&t=1666091160331&pageHeader=1&v=2')

# 1. 登录
phone = web.find_element('class name','ipt-tel')
pwd = web.find_element('class name','ipt-pwd')
login = web.find_element('class name','btn-big-blue')

phone.send_keys('16608855782')
pwd.send_keys('Dsq20020926')
login.click()
time.sleep(2)




while True:
