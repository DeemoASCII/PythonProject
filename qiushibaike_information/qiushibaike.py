#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:XiaoYang
import time
import re
import requests
from bs4 import BeautifulSoup
import pymysql
class QSBK(object):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='400810520',
            charset='utf8',
            database='qsbk'
        )
        self.cursor = self.conn.cursor()

    def get_response(self,url):
        s = 1
        res = self.session.get(url)
        if res.status_code == 200:
            return res.text
        print('请求失败，请等待{}秒后重试！！'.format(s))
        time.sleep(s)
        return self.get_response(url1)

    def get_userid(self,res):
        reg = r'href="/users/(.*?)/"'
        usersid = re.findall(reg, res)
        usersid = list(set(usersid))
        return usersid

    def parse_data(self,res):
        try:
            soup = BeautifulSoup(res,'lxml')
            username = soup.find('h2').text
            result = soup.find_all('div',class_ ='user-statis user-block')
            fans = result[0].select('li')[0].text
            praise = result[0].select('li')[4].text
            constellation = result[1].select('li')[1].text
            occupation = result[1].select('li')[2].text
            address = result[1].select('li')[3].text
            age = result[1].select('li')[4].text
            return username,fans,praise,constellation,occupation,address,age
        except IndexError as e:
            return None
    def save_mysql(self,data,i):
        # create_table = 'create table if not exists i(id INT PRIMARY KEY auto_increment,username VARCHAR (20) NOT NULL ,fans INT ,praise INT ,constellation VARCHAR (20),occupation VARCHAR (20),address VARCHAR (20),age INT)'
        # self.cursor.execute(create_table)
        insert_info = 'insert into i(username,fans,praise,constellation,occupation,address,age) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(insert_info,[str_split(item) for item in data])
            self.conn.commit()
            print('第{}条数据插入成功！'.format(i))
        except Exception as e:
            print(e)
            self.conn.rollback()

    def main(self,url1,url2):
            res = self.get_response(url1)
            userid = self.get_userid(res)
            for i in range(len(userid)):
                res = self.get_response(url2.format(userid[i]))
                data = self.parse_data(res)
                # print(data)
                self.save_mysql(data,i)




def str_split(info):
    return info.split(':')[-1]

if __name__ == '__main__':
    url1 = 'https://www.qiushibaike.com/8hr/page/{}/'
    url2 = 'https://www.qiushibaike.com/users/{}/'
    qsbk = QSBK()
    for page in range(1, 14):
        qsbk.main(url1.format(page),url2)