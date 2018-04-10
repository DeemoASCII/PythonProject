#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
from multiprocessing import Process,Manager
# #
# # a = 1
# #
# # def Func():
# #     global a
# #     a = 2
# # if __name__ == '__main__':
# #     p = Process(target=Func)
# #     p.start()
# #     p.join()
# #     print(a)
#
# if __name__ == '__main__':
#     mgr = Manager()  #启动服务器进程
#     d = mgr.dict()
#     # d = dict()
#     # print(type(d))
#
#     def func(d):
#         d['a'] = 'a'
#         print(d)
#
#     p = Process(target=func,args=(d,))
#     p.start()
#     p.join()
#     print(d)

import threading

# a = 1
#
# def func():
#     global a
#     a = 2
#
# t = threading.Thread(target=func)
# t.start()
# t.join()
# print(a)

# from multiprocessing import Queue  #线程队列
# import queue                       #普通的队列
# from multiprocessing import Manager
#
# q = queue.Queue()
# q.put(1)
# q.put(2)
# # print(q.get())
# q.put(3)
# print(q.full())  #判断队列是否满了
# print(q.qsize())  #返回队列长度

import threading
import random
import queue

class Producter(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            r = random.randint(0,9)
            # if self.queue.qsize() <9 :
            self.queue.put(r)
            print('添加了一个数据{}'.format(r))


class Customer(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # if not self.queue.empty():
            data = self.queue.get()
            print('从队列里面获取数据{}'.format(data))
            self.queue.task_done()

if __name__ == '__main__':
    q = queue.Queue(20)
    p1 = Producter(q)
    c1 = Customer(q)
    p1.start()
    c1.start()
    p1.join()
    c1.join()
    q.join()

