# coding=utf-8
import socketserver
import configparser

conf = configparser.ConfigParser()
conf.read('init.config')

ip_port = conf['HTTP']['ip_port']
size = conf['HTTP']['size']
backlog = conf['HTTP']['backlog']


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn是：', self.request)
        print('addr是：', self.client_address)

        while True:
            try:
                data = self.request.recv(int(size))
                if not data:
                    break
                print('收到客户端的消息是：', data.decode('utf8'))

                self.request.sendall(data.upper())
            except Exception:
                break

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(eval(ip_port), MyServer)
    s.serve_forever()
