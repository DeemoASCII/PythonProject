
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:XiaoYang
import pymysql
coon = pymysql.connect(
    host='localhost',user='root',password='400810520',db='qsbk',port=3306,charset='utf8'
)
cursor = coon.cursor()
create_table = 'create table if not exists i(id INT PRIMARY KEY auto_increment,username VARCHAR (20) NOT NULL ,fans INT ,praise INT ,constellation VARCHAR (20),occupation VARCHAR (20),address VARCHAR (20),age VARCHAR (10))'
sql = 'create table if not exists test(id INT PRIMARY KEY auto_increment,usename VARCHAR (20),password INT )'
insert_info ='''insert into test(usename,password) VALUES('肖','233')'''
cursor.execute(create_table)
coon.commit()
coon.close()