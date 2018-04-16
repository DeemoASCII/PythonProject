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
    task = [gevent.spawn(Blocking,i) for i in range(100)]
    gevent.joinall(task)

if __name__ == '__main__':
    start_time = time.time()
    Block_way()
    print('请求五次页面的耗时为：{}'.format(time.time() - start_time))


# #非阻塞改进
# import socket,time
# import selectors
#
# pn = 500
# sel = selectors.DefaultSelector()
# num_list = [i for i in range(pn)]
#
# class Crawler():
#     def __init__(self,word):
#         self.word = word
#         self.response = b''
#
#     def fetch(self):
#         client = socket.socket()
#         client.setblocking(False)
#         try:
#             client.connect(('www.baidu.com',80))
#         except BlockingIOError:
#             pass
#         sel.register(client,selectors.EVENT_WRITE,self.coon_send)
#
#     def coon_send(self,client):
#         sel.unregister(client)
#         request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(self.word))
#         client.send (request.encode())
#         sel.register(client,selectors.EVENT_READ,self.read)
#     def read(self,client):
#         global s
#         chunk = client.recv(1024)
#         if chunk:
#             self.response += chunk
#         else:
#             # print(self.response.decode())
#             sel.unregister(client)
#             num_list.pop()
#             if not num_list:
#                 s = True
#
# s = Falsermat(pn,time.time() - start_time))
# def loop():
#     while not s:
#         events = sel.select()
#         # print(events)
#         for key,mask in events:
#             callback = key.data
#             callback(key.fileobj)
#
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     for i in range(pn):
#         crawler = Crawler(i)
#         crawler.fetch()
#     loop()
#     print("请求{}次页面耗时为{}".fo