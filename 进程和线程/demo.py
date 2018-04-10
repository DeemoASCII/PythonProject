#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang

import time
import multiprocessing  #多进程模块
import threading

def func():
    # time.sleep(5)
    i = 0
    for _ in range(100000000):
        i += 1
    return True

def main():
    start_time = time.time()
    for i in range(4):
        p = multiprocessing.Process(target=func)  #创建一个子进程
        p.start()   #启动子进程
    # p = threading.Thread(target=func)  #创建一个子进程
    # p.start()   #启动子进程
    # func()
    func()
    end_time = time.time()
    print(end_time-start_time)

if __name__ == '__main__':
    main()