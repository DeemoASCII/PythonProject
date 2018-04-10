#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:XiaoYang
import socket
import threading

server = socket.socket()

server.bind(('',8888))

server.listen(5)

def Client(con,addr):
    '''

    :param con:
    :param addr:
    :return:
    '''
    while True:
        data = con.recv(1024)
        if data:
            print('{}:{}'.format(addr,data.decode()))
            con.send(data)
        else:
            print('客户端{}已关闭'.format(addr))
            break
    con.close()

while True:
    print('-----------主线程，等待客户端连接-----------')
    con,addr = server.accept()
    print('创建一个新的线程和客户端{}通信'.format(addr))
    client = threading.Thread(target=Client,args=(con,addr))
    client.start()