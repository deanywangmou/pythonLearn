# coding=utf-8

import select
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8080))
sk.listen()

# conn,addr=sk.accept()
# msg=conn.recv(1024)
# print('接受到消息是：',msg.decode('utf8'))
# conn.send(msg.upper())
#
# conn.close()
# sk.close()

while True:

    # 水平触发
    r, w, e = select.select([sk, ], [], [], 2)  # 2为设置等待时间
    for i in r:
        # conn, addr = i.accept()
        # print(conn)
        # print(addr)
        print('hello')

    print('>>>>>>>>>>>>>>>>')
