#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 10:42
# @Author  : XiaoYang
# @Site    : 
# @File    : 协程.py
# @Software: PyCharm
#
# from greenlet import greenlet
# import random
# import time
#
# def Producer():
#     while True:
#         item = random.randint(0,10)
#         print('生产了{}'.format(item))
#         c.switch(item) #切换到c
#         time.sleep(1)
#
#
# def Consumer():
#     while True:
#         item = p.switch()
#         print('消费了{}'.format(item))
#
# c = greenlet(Consumer)
# p = greenlet(Producer)
# c.switch()
#

from gevent import monkey;monkey.patch_all()
import gevent
from gevent.queue import Queue
import random

queue = Queue(5)

def producer(queue):
    while True:
        item = random.randint(0,10)
        print('生产了{}'.format(item))
        queue.put(item)

def consumer(queue):
    while True:
        item = queue.get()
        print('消费了{}'.format(item))

p = gevent.spawn(producer,queue)
c = gevent.spawn(consumer,queue)

gevent.joinall([p,c])


