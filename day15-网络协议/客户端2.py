# coding=utf-8
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机

phone.connect(('127.0.0.1', 8000))  # 拨通电话

phone.send('hello'.encode('utf-8'))

data = phone.recv(1024)
print('收到服务端的消息：', data.decode('utf8'))
phone.close()