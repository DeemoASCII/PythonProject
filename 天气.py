#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 14:14
# @Author  : XiaoYang
# @Site    : 
# @File    : 天气.py
# @Software: PyCharm


import re
import requests
import json
import random
import time

def get_url1(url1):
    r = requests.get(url1)
    dict_province = json.loads(r.text)      #把字符串转成字典
    #print(dict_province)
    #print('dict_province:',type(dict_province))
    city_dict = {}   #记录每一个省份的缩写  (类型ABC)
    for i in dict_province:
        #i 里面是每一个字典
        #print(i)
        #给字典赋值
        city_dict[i['name']] = i['code']
    province_city(city_dict)


def province_city(city_dict):
    for j in city_dict.values():
        place_url = 'http://www.nmc.cn/f/rest/province/'+j
        #print(place_url)
        get_url(place_url)  #把获取每一个省下面的每一个地区、


def get_url(url):
    m = requests.get(url)
    m.encoding = m.apparent_encoding
    #print(m.text)
    dict_place = json.loads(m.text)  # 把字符串转成字典
    #print('dict_place:',dict_place)
    #print('dict_place:',type(dict_place))

    #little_city_dict = {}
    for i in dict_place:
        # i 里面是每一个字典
        # print(i)
        # 给字典赋值
        little_city_dict[i['city']] = i['code']

def weather_url(little_city_dict):
    for k in little_city_dict.values():
        #[图片]http://www.nmc.cn/f/rest/real/57048?_=1525417963109
        url_random = str(random.randint(1500000000000, 1599999999999))
        weather_url = 'http://www.nmc.cn/f/rest/real/'+k+'?_='+url_random
        #print(weather_url)
        get_weather_url(weather_url)

def get_weather_url(weather_url):
    r = requests.get(weather_url)
    if r.status_code == 200:
        weather_json = json.loads(r.text)  # 把字符串转成字典
        #print("r.text:",r.text)
        #print("weather_json:",weather_json)
        li = []
        li.append(weather_json['station']['province'])
        li.append(weather_json['station']['city'])
        li.append(weather_json['publish_time'])
        li.append(weather_json['weather']['temperature'])
        li.append(weather_json['weather']['humidity'])
        li.append(weather_json['weather']['feelst'])
        li.append(weather_json['wind']['power'])
        li.append(weather_json['wind']['direct'])
        print("li:", li)
    else:
        time.sleep(1)
        get_weather_url(weather_url)



if __name__ == '__main__':

    little_city_dict = {}
    url1 = 'http://www.nmc.cn/f/rest/province'
    get_url1(url1)  #requests省份
    #print("每个城市的名称和id——little_city_dict:",little_city_dict)
    list_num = little_city_dict.items()
    num = 0
    for m in list_num:
        num += 1
    print("一共有：",num)
    weather_url(little_city_dict)