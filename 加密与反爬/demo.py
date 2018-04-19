#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 19:53
# @Author  : XiaoYang
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import re
import requests
import time
import urllib3
import base64
import json
import rsa
from binascii import b2a_hex
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


class Weibo_login():

    def __init__(self, user, pwd):
        urllib3.disable_warnings()  # 关闭警告
        self.session = requests.Session()
        self.session.verify = False  # 忽略证书认证
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        }
        self.user = user
        self.pwd = pwd

        pass

    def get_Time(self):
        '''
        get time str
        :return:
        '''
        return str(int(time.time() * 1000))

    def get_server_data(self):
        '''
         access pre_login_url
         get

        :return:
        '''
        data_dict = {
            'entry': 'weibo',
            'callback': 'sinaSSOController.preloginCallBack',
            'su': self.get_username(),
            'rsakt': 'mod',
            'checkpin': '1',
            'client': 'ssologin.js(v1.4.19)',
            '_': self.get_Time()
        }

        pre_login_url = 'https://login.sina.com.cn/sso/prelogin.php?'
        response = self.session.get(pre_login_url, headers=self.session.headers, params=data_dict,
                                    verify=self.session.verify)
        # print(response.text)
        if response.status_code == 200:
            html = response.text
            if html:
                json_data = re.findall(r'sinaSSOController.preloginCallBack\((.*?)\)', html)
                # 正则匹配sinaSSOController.preloginCallBack(）
                json_dict = json.loads(json_data[0])  # 把json str转换为字典
                # print(json_dict)
                self.servertime = json_dict['servertime']
                self.nonce = json_dict['nonce']
                self.rsakv = json_dict['rsakv']
                self.exectime = json_dict['exectime']
                self.pubkey = json_dict['pubkey']
                print('get_server_data servertime={} nonce={} rsakv={}'.format(self.servertime, self.nonce, self.rsakv))
            else:
                print('data is null')

        else:
            print('get_server_data response html error !!!')

    def login(self):
        """
        login weibo
        :return:
        """
        # preloginTimeStart = int(time.time()*1000)
        # temp_url = 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F&domain=.weibo.com&ua=php-sso_sdk_client-0.6.23&_rand=1523284754.9734'
        # parse_url = quote_plus(temp_url)  # 解码url
        # print(parse_url)
        # preloginTime = abs((int(time.time()*1000) - preloginTimeStart - self.exectime))  # 得到prelt

        login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        # login url
        username = self.get_username()  # get user name
        print('username base64=', username)

        pwd = self.get_pwd()
        print('pwd rsa =', pwd)

        data_dict = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'qrcode_flag': 'false',
            'useticket': '1',
            # 'pagerefer':parse_url,
            'vsnf': '1',
            'su': username,
            'service': 'miniblog',
            'servertime': self.servertime,
            'nonce': self.nonce,
            'pwencode': 'rsa2',
            'rsakv': self.rsakv,
            'sp': pwd,
            'sr': '1536*864',
            'encoding': 'UTF-8',
            'prelt': 18,
            'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        logining_page = self.session.post(login_url, data=data_dict, headers=self.session.headers)
        # logining_page.encoding = 'GBK'
        # print(logining_page.content.decode('GBK')) # <title>新浪通行证</title>
        login_loop = logining_page.content.decode('GBK')
        print(login_loop)
        pa = r'location\.replace\([\'"](.*?)[\'"]\)'
        loc = re.findall(pa, login_loop)
        print(loc)
        login_html = self.session.get(loc[0], headers=self.session.headers)
        login_content = login_html.content.decode('GBK')  # "正在登录 ..."
        if '正在登录' in login_content or 'Signing in' in login_html:
            pa = r'location\.replace\([\'](.*?)[\']\)'
            print('正在登录')
            cross_loc = re.findall(pa, login_content)
            # print(loc1)
            cross_html = self.session.get(cross_loc[0], headers=self.session.headers)
            cross_data = cross_html.content.decode('GBK')
            pa = r'parent.sinaSSOController\.feedBackUrlCallBack\((.*?)\)'
            feedback_data = json.loads(re.findall(pa, cross_data)[0])
            print(feedback_data)
            if feedback_data['result']:
                print("return result True")
                uniqueid = feedback_data['userinfo']['uniqueid']
                # print(uniqueid)
                main_html = self.session.get('https://weibo.com/u/{}/home'.format(uniqueid),
                                             verify=False).content.decode()
                soup = BeautifulSoup(main_html, 'lxml')
                main_title = soup.title.string
                print(main_title)  # 我的首页 微博-随时随地发现新鲜事
        else:
            print('用户登录失败')

    def get_username(self):
        """
        get base64 username
        返回必须是字符串
        :return:
        """
        username_quote = quote_plus(str(self.user))
        username_base64 = base64.b64encode(username_quote.encode('utf-8'))  # base64编码
        return username_base64.decode('utf-8')

    def get_pwd(self):
        """
         返回rsa加密的密码串
         返回必须是字符串
        :return:
        """
        rsa_publickey = int(self.pubkey, 16)  # 函数用于将一个字符串或数字转换为整型,把16进制字符转换为整型
        key = rsa.PublicKey(rsa_publickey, 65537)
        message = str(self.servertime) + '\t' + str(self.nonce) + '\n' + str(self.pwd)
        message = message.encode('utf-8')
        passwd = rsa.encrypt(message, key)
        passwd = b2a_hex(passwd).decode()  # 转换为16进制
        return passwd


if __name__ == '__main__':
    user_name = '18988037324'  # 用自己的用户和密码
    pwd = '400810520'
    wo = Weibo_login(user_name, pwd)
    wo.get_server_data()
    wo.login()
    # su = wo.get_username()
    # print(su)