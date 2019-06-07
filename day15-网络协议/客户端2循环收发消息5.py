# coding=utf-8
from socket import *
import configparser

conf = configparser.ConfigParser()

# 读取配置文件参数
conf.read('init.config')
ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']
print(type(ip_port), type(size), type(backlog))

# 编写客户端
tcp_client = socket(AF_INET, SOCK_STREAM)

# 建立与服务端的连接
tcp_client.connect(eval(ip_port))

while True:
    msg = input('请输入信息：').strip()
    # 向服务端发送消息

    if not msg:
        continue

    tcp_client.send(msg.encode('utf8'))
    print('向服务端发送消息是：')

    # 接收服务端发来的消息
    data = tcp_client.recv(int(size))
    print('服务端发来的消息是：', data.decode('utf8'))

tcp_client.close()
