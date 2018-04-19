#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 17:50
# @Author  : XiaoYang
# @Site    :
# @File    : 加密.py
# @Software: PyCharm
#MD5加密
# import hashlib
#
# s = b'xiaoyue'
# m = hashlib.md5()
# m.update(s)
# print(m.hexdigest())

# #base64
# from Cryptodome.Cipher import DES
#
# key = '1515610895'
# des = DES.new(key.encode(),DES.MODE_ECB)
# text = '1515610895  '
# encrypto_text = des.encrypt(text.encode())
# print(encrypto_text)
# print(des.decrypt(encrypto_text))

# import rsa
# import binascii
#
# pubkey,privkey = rsa.newkeys(2048)#  生成公钥和私钥
#
# def rsaEmcrypt(text):
#     encrypt_text = rsa.encrypt(text.encode(),pubkey)
#     return binascii.b2a_hex(encrypt_text)
#
# def rsaDecrypt(text):
#     decrypt_text = rsa.decrypt(binascii.a2b_hex(text),privkey)
#     return decrypt_text
#
# # print(rsaEmcrypt('hellow world'))
# # print(rsaDecrypt(rsaEmcrypt('hellow world')))
# print(pubkey,privkey)
#
# s = rsa.PublicKey(2,3)
# M = rsa.encrypt('115423'.encode(),s)
# print('shengchengde shi {}'.format(M))

#

import base64
import time
import binascii
import rsa
import urllib.request

encode = base64.b64encode(b'1515610895')
print(encode)
s = time.time()
print(s)
print(round(s,4))
pubkey = (165138424261149263963666229661164814908887524950166142962960019363944425161240370251403452452001165143400173133423045791330687304650944332950460079059702342999940532642226896299225258939028313437520982527474148958262129523279095471616009516621824844891755906467794220597075349492626446841979774101805104112707, 65537)
data = 'de5f45b4bda90b446d1b99e450d3bbd581bb8dff510c8977a86f463899df564f1f3d4d7b61be37a42ae4aa026f30254731ccbfbd8649b89283568201986d68fb2141a038abe65715d76391ab4300f0c2ba75dffcb61798dfc0236c64ba44ec119012819a8dcc952e8d5aaf76be87f44f08b561db2b62786a5025b0db23e137bc'
word = '1524106709' +'\t'+'3PO80B'+'\n'+'400810520'
# sp = rsa.encrypt(word.encode(),pubkey)
# print(sp)
a = binascii.a2b_hex(data.encode())
print(a)