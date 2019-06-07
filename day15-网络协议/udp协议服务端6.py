# coding=utf-8
from socket import *
import configparser

conf=configparser.ConfigParser()
conf.read('init.config')

ip_port=conf['HTTP']['ip_port']
size=conf['HTTP']['size']

print(ip_port,size)

udp_service=socket(AF_INET,SOCK_DGRAM)
udp_service.bind(eval(ip_port))

while True:
    data,addr=udp_service.recvfrom(eval(size))
    print(data.decode('utf-8'))
    print(addr)

    udp_service.sendto(data.upper(),addr)


