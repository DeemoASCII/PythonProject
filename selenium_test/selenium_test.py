#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:11
# @Author  : XiaoYang
# @Site    : 
# @File    : selenium_test.py
# @Software: PyCharm

# import time
# import json
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

# 输入点击
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# try:
#     print(driver.page_source)
#     driver.find_element_by_id('kw').send_keys('python')
#     driver.find_element_by_id('su').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
#     # driver.find_element_by_link_text('贴吧').click()
#     # driver.save_screenshot('test.png')
# finally:
#     time.sleep(50)
#     driver.close()

#拖动
# driver = webdriver.Chrome()
# driver.get('https://passport.damai.cn/login')
#
# try:
#     # print(driver.page_source)
#     time.sleep(15)
#     cookies = driver.get_cookies()
#     print(cookies)
#     cookies_dict = {}
#     for item in cookies:
#         cookies_dict[item.get('name')] = item.get('value')
#     with open('cookies.txt','w') as f:
#         f.write(json.dumps(cookies_dict,ensure_ascii=False,indent=4))
#     time.sleep(10)
#     # driver.find_element_by_id('fm-login-id').clear()
#     # ActionChains(driver).click(driver.find_element_by_class_name('login-tabs-tab active')).perform()
#     # driver.find_element_by_id('fm-login-id').send_keys('18988037324')
#     # driver.find_element_by_id('fm-login-password').send_keys('xiaoyue1314')
#     # driver.find_element_by_class_name('fm-button fm-submit ').click()
#
# finally:
#     time.sleep(10)
#     driver.close()
#
# with open('cookies.txt','r',encoding='utf-8') as f:
#     cookies_dict = json.loads(f.read())
#
# res = requests.get('https://www.damai.cn/',cookies=cookies_dict,timeout=5,allow_redirects=False)
# if res.status_code == 200:
#     print(res.content.decode('utf-8'))

# from requests_html import HTMLSession
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium\
#     .webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
#
# element = (By.ID,'kw')  #事件
# try:
#     WebDriverWait(driver,20,0.5).until(EC.presence_of_all_elements_located(element))#当条件城里的时候才会返回，否则在超时的神时间之内都会不断的检测
#     driver.find_element_by_id('kw').send_keys('python')
#
#
# finally:
#     time.sleep(5)
#     driver.close()

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.weibo.com')
driver.maximize_window()
try:
    wait = WebDriverWait(driver,20,0.5)

    wait.until(EC.presence_of_all_elements_located((By.ID,'loginname')))
    wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')))
    username = driver.find_element_by_id('loginname')
    username.clear()
    time.sleep(1)
    username.send_keys('18988037324')
    password = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
    time.sleep(1)
    password.send_keys('400810520')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    print(driver.page_source)
except Exception as e:
    print(e)
finally:
    time.sleep(10)
    driver.close()

