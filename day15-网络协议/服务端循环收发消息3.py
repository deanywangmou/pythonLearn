# coding=utf-8
from socket import *
import configparser

# 将变量写入配置文件中
conf = configparser.ConfigParser()
conf["HTTP"] = {
    'ip_port': '("127.0.0.1",8002)',
    'size': '1024',
    'backlog': '5'
}

conf['DEFAULT'] = {}
setconf = conf['DEFAULT']
setconf['name'] = 'tcp_server'
setconf['file'] = 'init.config'

with  open('init.config', 'w') as f:
    conf.write(f)

# 读取配置文件参数
conf.read('init.config')
ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']
print(type(ip_port), type(size), type(backlog))
print(type(eval(ip_port)), type(int(size)), type(int(backlog)),size,backlog)

# 编写服务端
tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(eval(ip_port))

tcp_server.listen(int(backlog))

while True:
    print('服务端开始运行了')

    # 建立与客户端的连接
    conn, addr = tcp_server.accept()
    print('双向链接是：',conn)
    print('客户端地址是：',addr)

    #循环收发消息
    while True:
        try:
            # 接收消息
            msg = conn.recv(int(size))
            '''注意：unix系统直接中断客户端不会报错，需要改成if not msg:break进行判断'''
            print('客户端发来的消息是：', msg.decode('utf8'))

            # 向客服端发送消息
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()
tcp_server.close()
