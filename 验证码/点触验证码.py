#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 15:13
# @Author  : XiaoYang
# @Site    : 
# @File    : 点触验证码.py
# @Software: PyCharm

import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .chaojiying import Chaojiying

Chaojiying_username = '1021054331'
Chaojiying_password = '400810520'
Chaojiying_soft_id = 896503
Chaojiying_kind = 9004

class CrackTouClick():
    def __init__(self):
        self.url = 'http://dun.163.com/trial/picture-click'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10,0.5)
        self.chaojiying = Chaojiying(Chaojiying_username,Chaojiying_password,Chaojiying_soft_id)

    def __del__(self):
        self.driver.close()

    def open(self):
        '''
        打开网页 最大化 操作滚动条
        :return:
        '''
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        js = 'var q=document.documentElement.scrollTop=100'
        self.driver.execute_script(js)

    def get_touclick_element(self):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/img[1]')))
        return element

    def get_points(self,result):
        groups = result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')]for group in groups]
        # print(locations)
        return locations

    def touch_click_words(self,locations):
        if len(locations) == 3:
            print(locations)
            for location in locations:
                ActionChains(self.driver).move_to_element_with_offset(self.get_touclick_element(),location[0],location[1]).click().perform()
                time.sleep(1)
        else:
            s = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/div/div[3]')
            s.click()
            self.main()

    def get_touclick_image(self,name='captcha.png'):
        '''
        获取图片
        :param name:
        :return:
        '''
        time.sleep(2)
        self.driver.save_screenshot('aa.png')
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div')
        left = element.location['x']
        top = element.location['y'] - 100
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height'] - 100
        im = Image.open('aa.png')
        captcha = im.crop((left,top,right,bottom))
        # captcha.show()
        captcha.save(name)
        return captcha

    def main(self):
        self.get_touclick_element()
        image = self.get_touclick_image()
        bytes_arry = BytesIO()
        image.save(bytes_arry,format('PNG'))
        result = self.chaojiying.post_pic(bytes_arry.getvalue(),Chaojiying_kind)
        # print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)
        # time.sleep(10)
        try:
            success = self.wait.until(EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[2]/div[3]/span[2]'),'验证成功'))
        except:
            print('验证失败，重新上传验证')
            self.main()
        else:
            self.driver.save_screenshot('True.png')
            print(success)

if __name__ == '__main__':
    crack = CrackTouClick()
    crack.open()
    crack.main()
