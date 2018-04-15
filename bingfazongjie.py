#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 15:46
# @Author  : XiaoYang
# @Site    : 
# @File    : bingfazongjie.py
# @Software: PyCharm

import socket
import time

#zuse
# def Blocking(word):
#     client = socket.socket()
#     client.connect(('www.baidu.com',80))
#     request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(word))
#     client.send(request.encode())
#     respose = b''
#     chunk = client.recv(1024)
#     while chunk:
#         respose += chunk
#         chunk = client.recv(1024)
#     # print(respose.decode())
#     return respose
#


##非阻塞
# def Blocking(word):
#     client = socket.socket()
#     client.setblocking(False)
#     try:
#         client.connect(('www.baidu.com',80))
#     except BlockingIOError:
#         pass
#     request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(word))
#     while True:
#         try:
#             client.send(request.encode())
#             break
#         except OSError:
#             pass
#
#     respose = b''
#     while True:
#         try:
#             chunk = client.recv(1024)
#             while chunk:
#                 respose += chunk
#                 chunk = client.recv(1024)
#             break
#         except BlockingIOError:
#             pass
#     # print(respose.decode())
#     return respose
#

##多线程
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
from gevent import monkey;monkey.patch_all()
import gevent

def Blocking(word):
    client = socket.socket()
    client.connect(('www.baidu.com',80))
    request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(word))
    client.send(request.encode())
    respose = b''
    chunk = client.recv(1024)
    while chunk:
        respose += chunk
        chunk = client.recv(1024)
    # print(respose.decode())
    return respose

def Block_way():
    # pool = ThreadPool(5)
    # for i in range(5):
    #     pool.apply_async(Blocking,args=(i,))
    # pool.close()
    # pool.join()
    task = [gevent.spawn(Blocking,i) for i in range(5)]
    gevent.joinall(task)

if __name__ == '__main__':
    start_time = time.time()
    Block_way()
    print('请求五次页面的耗时为：{}'.format(time.time() - start_time))
