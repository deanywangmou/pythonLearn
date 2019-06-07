# coding=utf-8
# 不能名称定位socket
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 加这条就不会出现重启服务器时报端口占用的情况
phone.bind(('127.0.0.1', 8000))  # 绑定电话卡

phone.listen(5)  # 开机

print('-------->')
conn, addr = phone.accept()  # 等电话
# print(conn,addr)
msg = conn.recv(1024)  # 收消息
print('客户端发来的消息是：', msg)

conn.send(msg.upper())

conn.close()
phone.close()
