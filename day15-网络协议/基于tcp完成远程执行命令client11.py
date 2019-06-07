# coding=utf-8
import configparser
from socket import *

conf = configparser.ConfigParser()

# 读取配置文件参数
conf.read('init.config')
ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']
print(type(ip_port), type(size), type(backlog))

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(eval(ip_port))

while True:
    cmd=input('请输入执行命令：').strip()
    if not cmd:
        continue
    if cmd=='quit':
        break

    tcp_client.send(cmd.encode('utf8'))
    cmd_res=tcp_client.recv(int(size))
    print('收到服务端返回的消息是：',cmd_res.decode('gbk'))

tcp_client.close()
