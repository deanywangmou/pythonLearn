# coding=utf-8
import time
from socket import *
import configparser

conf = configparser.ConfigParser()
conf.read('init.config')

ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']

print(ip_port, size)

ntp_server = socket(AF_INET, SOCK_DGRAM)
ntp_server.bind(eval(ip_port))

while True:
    data, addr = ntp_server.recvfrom(int(size))
    if not data:
        fmt = '%Y-%m-%d %X'
    else:
        fmt = data.decode('utf8')

    ntp_server.sendto(time.strftime(fmt).encode('utf8'), addr)
