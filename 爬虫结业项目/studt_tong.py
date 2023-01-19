"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : studt_tong.py
@Author : 夏目&青一
@Time : 2022/10/11 16:13

"""

"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : qqmusic.py
@Author : 夏目&青一
@Time : 2022/10/11 14:06

"""
# 学习通的网址  http://i.mooc.chaoxing.com/space/index?t=1665473483111
from selenium import webdriver
import time
user = '16608855782'
password = 'Dsq20020926'

xxi= 'http://i.mooc.chaoxing.com/space/index?t=1665473483111'
borw = webdriver.Chrome()
borw.get(xxi)
borw.find_element_by_xpath('//*[@id="phone"]').send_keys(user)
borw.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
time.sleep(2)
borw.find_element_by_tag_name('button').click()
borw.find_element_by_xpath('//*[@id="course_221258875_60766047"]/div[1]/a/img').click() #点击web开发
borw.implicitly_wait(10)

time.sleep(2000)


# https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=491661319&courseId=221258875&clazzid=60766047&cpi=217041836&enc=0373c151642e357a3d66d23e7189fe5c&mooc2=1&openc=c77fb5cb604603c5dde527ba1a8a151f
# https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=491661748&courseId=221258875&clazzid=60766047&cpi=217041836&enc=0373c151642e357a3d66d23e7189fe5c&mooc2=1&openc=c77fb5cb604603c5dde527ba1a8a151f
borw.quit()


