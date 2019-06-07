# coding=utf-8
from socket import *
import configparser

conf=configparser.ConfigParser()
conf.read('init.config')

ip_port=conf['HTTP']['ip_port']
size=conf['HTTP']['size']

print(ip_port,size)

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('请输入数据：').strip()
    udp_client.sendto(msg.encode('utf8'),eval(ip_port))

    data,addr=udp_client.recvfrom(eval(size))
    print(data.decode('utf8'))
    print(addr)





