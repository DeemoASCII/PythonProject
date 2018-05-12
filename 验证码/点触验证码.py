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