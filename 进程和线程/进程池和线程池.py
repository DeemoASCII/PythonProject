#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
#
# import threading
# import queue
#
# class MyThread(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.queue = queue.Queue()
#         self.daemon = True
#
#     def run(self):
#         while True:
#             func = self.queue.get()
#             func()
#             self.queue.task_done()
#
#     def apply_async(self,func):
#         self.queue.put(func)
#
#     def join(self):
#         self.queue.join()
#
#
# def func1():
#     print('func1')
#
# def funv2():
#     print('func2')
#
# t = MyThread()
# t.start()
# t.apply_async(func1)
# t.apply_async(funv2)
# t.join()
#
# import threading
#
# class Worker(threading.Thread):
#     def __init__(self):
#         super().__init__()
#

from multiprocessing.pool import ThreadPool   #线程池
from multiprocessing import  Pool     #进程池
import time
import random

def worker(msg):
    t_start = time.time()
    data = random.randint(0,9)
    print('111')

pool = ThreadPool(4)

pool.apply_async(worker)
# pool.map()
pool.close()
pool.join()