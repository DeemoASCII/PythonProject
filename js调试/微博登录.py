#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 10:34
# @Author  : XiaoYang
# @Site    : 
# @File    : 微博登录.py
# @Software: PyCharm

import time
import re
import json
import requests
import urllib3
import base64
import binascii
import rsa

urllib3.disable_warnings()

class WeiBo(object):
    def __init__(self,username,password):
        self.username = str(username)
        self.password = str(password)
        self.s = requests.session()
        self.s.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        self.s.verify = False

    def Get_data(self):
        self.su = base64.b64encode(self.username.encode()).decode()
        # su = urllib.request.quote(self.su)
        # print(self.su)
        data = {
            'entry': 'weibo',
            'callback': 'sinaSSOController.preloginCallBack',
            'su': self.su,
            'rsakt': 'mod',
            'checkpin': '1',
            'client': 'ssologin.js(v1.4.19)',
            '_': int(time.time()*1000)
        }
        url = 'https://login.sina.com.cn/sso/prelogin.php?'
        # print(url)
        res = self.s.get(url,params=data)
        reg = re.findall(r'''preloginCallBack\((.*?)\)''',res.text)[0]
        json_data = json.loads(reg)
        # print(res.text)
        # self.pubkey = re.findall(r'''"pubkey":"(.*?)"''',res.text)[0]
        # self.rsakv = re.findall(r'''"rsakv":"(.*?)"''',res.text)[0]
        # self.nonce = re.findall(r'''"nonce":"(.*?)"''',res.text)[0]
        # self.servertime = re.findall(r'''"servertime":(.*?),"pcid"''',res.text)[0]
        self.pubkey = json_data['pubkey']
        self.rsakv = json_data['rsakv']
        self.nonce = json_data['nonce']
        self.servertime = json_data['servertime']

    def Login(self):
        self.Get_data()
        pubkey = rsa.PublicKey(int(self.pubkey,16),int('10001',16))
        word = str(self.servertime) + '\t' + str(self.nonce) + '\n' + str(self.password)
        self.sp = rsa.encrypt(word.encode(),pubkey)
        self.sp = binascii.b2a_hex(self.sp).decode()
        # print(self.sp)
        url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        data = {
            'entry':'weibo',
            'gateway':'1',
            'from':'',
            'savestate':'7',
            'qrcode_flag':'false',
            'useticket':'1',
            'vsnf':'1',
            'su':self.su,
            'service':'miniblog',
            'servertime':self.servertime,
            'nonce':self.nonce,
            'pwencode':'rsa2',
            'rsakv':self.rsakv,
            'sp':self.sp,
            'sr':'1920*1080',
            'encoding':'UTF-8',
            'prelt':30,
            'url':'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype':'META',
        }
        # data = parse.urlencode(data)
        # print(data)
        res1 = self.s.post(url,data=data)
        res1.encoding = 'GBK'
        # print(res1.content.decode('GBK')
        reg = re.findall(r'''location.replace\("(.*?)"\)''',res1.text)[0]
        url2 = reg
        # print(url2)
        res2 = self.s.get(url2)
        res2.encoding = 'GBK'
        if '正在登录' in res2.text:
            reg = re.findall(r'''location.replace\('(.*?)'\)''',res2.text)[0]
            url3 = reg
            res3 = self.s.get(url3)
            res3.encoding = 'GBK'
            result = re.findall(r'''"result":(.*?),''',res3.text)[0]
            if result == 'true':
                print('登录成功，即将跳转到个人主页！')
                time.sleep(5)
                uniqueid = re.findall(r'''"uniqueid":"(.*?)"''',res3.text)[0]
                url4 = 'https://weibo.com/u/{}/home'.format(uniqueid)
                res4 = self.s.get(url4)
                print(res4.text)
            else:
                print('登录失败。。。')
        else:
            print('登录失败。。。')


if __name__ == '__main__':
    p = WeiBo(11111,11111)
    p.Login()

