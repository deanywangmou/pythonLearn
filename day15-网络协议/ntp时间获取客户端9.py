# coding=utf-8
from socket import *
import configparser

conf = configparser.ConfigParser()
conf.read('init.config')

ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']

print(ip_port, size)

ntp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('请输入时间格式：').strip()
    ntp_client.sendto(msg.encode('utf8'), eval(ip_port))

    data, addr = ntp_client.recvfrom(int(size))
    print('ntp服务器的标注时间为：', data.decode('utf8'))
