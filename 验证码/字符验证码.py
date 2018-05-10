#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 21:35
# @Author  : XiaoYang
# @Site    : 
# @File    : 字符验证码.py
# @Software: PyCharm

from PIL import Image

# # image = Image.open('code.jpg')
# # image.show()
# # print(image.size)
#
def binaring(image,threshold = 150):
    '''
    对传入的图像进行灰度和二值化处理
    :param image:
    :param threshold:
    :return:
    '''
    image = image.convert('L')
    pixdata = image.load()
    w,h = image.size
    for y in range(h):
        for x in range(w):
            if pixdata[x,y] < threshold:
                pixdata[x,y] = 0
            else:
                pixdata[x,y] = 255

    return image

def depoint(image):
    '''
    对传入的图片降噪
    :param image:
    :return:
    '''
    pixdata = image.load()
    w,h = image.size

    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count += 1
            if pixdata[x,y+1] > 245:
                count += 1
            if pixdata[x-1,y] > 245:
                count += 1
            if pixdata[x+1,y] > 245:
                count += 1
            if count > 3:
                pixdata[x,y] = 255
    return image
#
# image = Image.open('code.jpg')
# im = binaring(image=image)
# im.show()
# im = depoint(im)
# im.show()

from pytesser3 import image_to_string

image = Image.open('code.jpg')
image = binaring(image)
image = depoint(image)
print(image_to_string(image))