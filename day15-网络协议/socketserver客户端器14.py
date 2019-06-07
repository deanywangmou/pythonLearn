# coding=utf-8
from  socket import *
import  configparser

conf=configparser.ConfigParser()
conf.read('init.config')

ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']

tcp_clent=socket(AF_INET,SOCK_STREAM)

tcp_clent.connect(eval(ip_port))

while True:
    msg=input('请输入信息：').strip()
    if  not msg:
        continue
    if msg=='quit':
        break

    tcp_clent.send(msg.encode('utf8'))

    data=tcp_clent.recv(int(size))
    print('收到服务端发来的消息：',data.decode('utf8'))
