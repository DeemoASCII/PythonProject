#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:XiaoYang
from socket import socket
s = socket()
# print(s)
s.bind(('',1234)) #服务端套接字  绑定1234端口
print(s)