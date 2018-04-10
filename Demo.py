#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
import re
import  requests
from bs4 import BeautifulSoup
import random
import time
import  xlwt
import pymysql

class China_energy():  #get 类


    def __init__(self):
        self.list_model = []  # 存放机型
        self.list_title = []  # 存放产品名称
        self.list_time = []  # 存放备案公布时间
        self.list_company = []  # 存放公司
        self.list_id = []  # 存放id
        self.list_energy = []  # 能效标识

        self.list_type = []  # 产品类型
        self.list_energy_index = []  # 液晶电视能效指数
        self.list_power = []  # 液晶电视被动待机功率（W）


    def url_get(self,url):
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,'html.parser')
            # print("soup:",soup)
            # print("r.text",r.text)
            # print("soup_type:", type(soup))
            # print("r.text_type", type(r.text))
            return r
        print("请求失败， 等待1秒从新尝试".format(1))
        time.sleep(1)
        return self.url_get(self,url)  #从新调用url_get函数获取网页

class url_Parse(China_energy):   #解析类

    def no_Detail(self,soup):


        #爬去当前页面的id 1、
        id = re.findall('"id":(\d{8})',soup)
        print("id11111:",id)

        # 爬去当前页面的id 2、
        id1 = re.findall('"id":\d{8}', soup)
        p = re.compile('"id":(\d{8})')    #需要这个id 字典values对应的值，就需要加上括号
        for i in id1:
            l1 = p.findall(i)
            #print("l1:",type(l1))
            self.list_id.append(l1[0])      #
            l1 = str(l1[0])
            #print(type(l1))
        print("list_id:",self.list_id)



        # 爬去当前页面的机型1、
        model1 = re.findall(r'"markingTitle":"(.*?)"',r.text)   #两种方法  这个是第一个比较简单， 直接在r.text里面取
        print("model1:",model1)                                  #(r'"markingTitle":"(.*?)"',r.text)  的（.*?）就是去字典values的方法


        #爬去当前页面的机型2、
        model = re.findall(r'"markingTitle":".*?"',r.text)
        #print("model:",model)
        m = re.compile(r'"markingTitle":"(.*?)"')
        for i in model:
            l2 = m.findall(i)
            self.list_model.append(l2[0])
        print("markingTitle:",self.list_model)




        # 爬去产品名称1、
        title1 = re.findall(r'"modelTitle":"(.*?)"', r.text)
        print('title1:', title1)
        #爬去产品名称2、
        title = re.findall(r'\"modelTitle\"\:\".*?\"', r.text)
        #print('title:',title)
        n = re.compile('"modelTitle":"(.*?)"')
        for i in title:
            l3 = n.findall(i)
            self.list_title.append(l3[0])
        print("平板电视:",self.list_title)



        # 爬去时间1、
        time1 = re.findall(r'"bulletInTime":"(.*?)"', r.text)
        print("time1",time1)
        # 爬去时间2、
        time = re.findall(r'\"bulletInTime\"\:\".*?\"', r.text)
        q = re.compile('"bulletInTime":"(.*?)"')
        for i in time:
            l4 = q.findall(i)
            self.list_time.append(l4[0])
        print("时间是:",self.list_time)


        #生产公司
        #company = re.findall(r'\"entallname\"\:\".*?\"', r.text)
        company = re.findall(r'"entallname":"(.*?)"', r.text)
        print(company)
        # e = re.compile('"entallname":"(.*?)"')
        # for i in company:
        #     l5 = e.findall(i)
        #     self.list_company.append(l5[0])
        # print("生产厂家：",self.list_company)

        # 能效等级
        energy = re.findall('"markingLevel":(\d)', r.text)
        print('energy:',energy)
        en = re.compile('"markingLevel":(\d)')
        # for i in energy:
        #     l6 = en.findall(i)
        #     self.list_energy.append(l6[0])
        # print("能效等级")

p = url_Parse()
p.url = 'https://www.energylabelrecord.com:12066/productpub/list.do?ec_model_no=24&type=markingTitle&typeValue=&pageNum=1&pageSize=15&_=1522637289995'
#print(p.url_get(p.url))
r = p.url_get(p.url)
p.no_Detail(r.text)
