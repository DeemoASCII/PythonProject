#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
import socket

c = socket.socket()

c.connect(('127.0.0.1',8888))

while True:
    msg = input('>>>')
    if msg == 'quit':
        break
    c.send(msg.encode())
    data = c.recv(1024)
    print(data.decode())