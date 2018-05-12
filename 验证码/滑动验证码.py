#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 17:13
# @Author  : XiaoYang
# @Site    : 
# @File    : 滑动验证码.py
# @Software: PyCharm

import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from requests_html import HTMLSession
from io import BytesIO
import random

s = HTMLSession()
div_path1 = '//*[@class="gt_cut_bg gt_show"]/div'
div_path2 = '//*[@class="gt_cut_fullbg gt_show"]/div'


def merge_imgae(image_file,location_list):
    im = Image.open(image_file)
    # im.show()
    new_im = Image.new('RGB',(260,116))
    im_list_upper = []
    im_list_down = []
    for location in location_list:
        # print(location['y'])
        if location['y'] == -58:
            result = im.crop((abs(location['x']),58,abs(location['x'])+10,116))
            im_list_upper.append(result)
        else:
            result = im.crop((abs(location['x']),0,abs(location['x'])+10,58))
            im_list_down.append(result)
    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im,(x_offset,0))
        x_offset += im.size[0]
    x_offset = 0
    for im in im_list_down:
        new_im.paste(im,(x_offset,58))
        x_offset += im.size[0]
    # new_im.show()
    return new_im


def get_image(driver,div_path):
    time.sleep(2)
    background_images = driver.find_elements_by_xpath(div_path)
    print(len(background_images))
    location_list = []
    for background_image in background_images:
        # print(background_image)
        location = {}
        reg = re.compile(r'''background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;''',re.S)
        result = re.findall(reg,background_image.get_attribute('style'))
        # print(result)
        location['x'] = int(result[0][1])
        location['y'] = int(result[0][2])
        image_url = result[0][0]
        # print(image_url)
        location_list.append(location)
    print('================================================')
    image_url = image_url.replace('webp','jpg')
    image_result = s.get(image_url).content
    # with open('滑动验证码.jpg','wb') as f:
    #     f.write(image_result)
    #     f.close()
    image_file = BytesIO(image_result)   #s是一张无序的图片
    image = merge_imgae(image_file,location_list)
    return image


def is_simpil(image1,image2,x,y):
    '''
    对比RGB值来发现渠口
    :param image1:
    :param image2:
    :param x:
    :param y:
    :return:
    '''
    pixel1 = image1.getpixel((x,y))
    pixel2 = image2.getpixel((x,y))
    for i in range(3):
        if abs(pixel1[i] - pixel2[i]) >= 50:
            return False
    return True

def get_move_location(image1,image2):
    for i in range(0,260):
        for j in range(0,116):
            if is_simpil(image1,image2,i,j) == False:
                return i

def get_track(l):
    track = []
    current = 0
    mid = l*3/5
    t = 0.2
    v = 0
    while current < l:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a*t
        move = v0*t + 0.5*a*t*t
        current += move
        track.append(round(move))

    for i in range(5):
        track.append(-1)
    return track


def main(driver):
    driver.get('http://www.cnbaowen.net/api/geetest/')
    element = WebDriverWait(driver,10,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'gt_slider_knob')))
    image1 = get_image(driver,div_path1)
    image2 = get_image(driver,div_path2)
    l = get_move_location(image1,image2)
    track_list = get_track(l)
    print('点击滑动按钮')
    ActionChains(driver).click_and_hold(on_element=element).perform()
    time.sleep(1)
    print('拖动滑动按钮')
    for track in track_list:
        ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-1,yoffset=0).perform()
    # time.sleep(1)
    print('释放鼠标！')
    ActionChains(driver).release(on_element=element).perform()
    time.sleep(10)

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        main(driver)
    finally:
        driver.close()