#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
import selectors
import time
from socket import socket

# sel = selectors.EpollSelector()             #选择一种多路复用的技术  windows选择DefultSelect    Linux用epoll
sel = selectors.DefaultSelector()

server = socket()
server.bind(('',8989))
server.listen(5)

#注册事件
def Read(con):
    data = con.recv(1024)
    if data:
        print(data.decode())
        con.send(data)
    else:
        print('关闭客户端{}'.format(con))
        sel.unregister(con)
        con.close()
        exit()

def Accept(server):
    con,addr = server.accept()
    print('客户端{}连接成功！'.format(addr))
    sel.register(con,selectors.EVENT_READ,Read)

sel.register(server,selectors.EVENT_READ,Accept)  #当客户端连接了  该怎么办

while True:
    events = sel.select()  #返回有变化的套接字

    for key,mask in events:
        # print(key)
        # time.sleep(5)
        callback = key.data
        callback(key.fileobj)
