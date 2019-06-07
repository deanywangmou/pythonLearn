# coding=utf-8
import configparser
import subprocess
from socket import *

conf = configparser.ConfigParser()

# 读取配置文件参数
conf.read('init.config')
ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']
print(type(ip_port), type(size), type(backlog))

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(eval(ip_port))
tcp_server.listen(int(backlog))

while True:
    conn, addr = tcp_server.accept()
    print('双向链接是：', conn)
    print('客户端地址是：', addr)

    while True:
        try:
            cmd = conn.recv(int(size))
            if not cmd:
                break
            print('收到客户端的命令：', cmd)

            # 执行命令，得到命令的运行结果cmd
            res = subprocess.Popen(cmd.decode('utf8'), shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()

            if not cmd_res:
                cmd_res='执行成功'.encode('gbk')

            print(cmd_res.decode('gbk'))
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break

    conn.close()
tcp_server.close()
