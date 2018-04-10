#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:XiaoYang

from bs4 import BeautifulSoup
import requests
from lxml import etree

html = requests.get('http://www.baidu.com/s?wd=python').text
soup = BeautifulSoup(html,'lxml')
print(soup)
# e = etree.HTML(html)
# for i in e.xpath('//p'):
#     print(i.text)
