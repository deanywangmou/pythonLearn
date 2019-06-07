# coding=utf-8

import select
import socket

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',8080))

sk.send('hello python'.encode('utf8'))
data=sk.recv(1024)
print(data.decode('utf8'))

