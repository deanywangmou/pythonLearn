# coding=utf-8
import hashlib

obj = hashlib.md5()
obj.update('hello'.encode('utf8'))
print(obj.hexdigest())

obj.update('root'.encode('utf8'))
print(obj.hexdigest())  # 打印出来的是root和hello的加密

m=hashlib.md5()
m.update('helloroot'.encode('utf8'))
print(m.hexdigest())