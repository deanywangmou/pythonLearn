# coding=utf-8
import socketserver
import json
import configparser
from config import setting
import os

STATUE_CODE = {
    254: '验证通过',
    254: '验证失败',
    801: '文件已存在',
    800: '文件已存在，但是不全,是否继续',
    802: '文件不存在'
}


class HanderServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            data = json.loads(data.decode('utf8'))

            '''
            {'action':'auth',
              'username':'yuan',
              'pwd':'123'
            }
            '''

            if data.get('action'):
                if hasattr(self, data.get('action')):
                    func = getattr(self, data.get('action'))
                    func(**data)
                else:
                    print('Invalid cmd')
            else:
                print('输入的信息无效')

    def auth(self, **data):
        print('data', data)
        username = data['username']
        password = data['password']
        user = self.authenticate(username, password)

        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def send_response(self, status_code):
        response = {'status_code': status_code,
                    'status_msg': ''}
        self.request.sendall(json.dumps(response).encode('utf8'))

    def authenticate(self, user, pwd):
        cfg = configparser.ConfigParser()
        cfg.read(setting.ACCOUNT_PATH)

        if user in cfg.sections():
            if cfg[user]['password'] == pwd:
                self.mainPath = os.path.join(setting.BASE_DIR, 'home', self.user)
                self.user = user
                print('密码正确')
                return user

    def put(self, **data):
        print('data', data)
        file_name = data.get('file_name')
        file_siza = data.get('file_siza')
        target_path = data.get('target_path')

        abs_path = os.path.join(self.mainPath, target_path, file_name)

        has_receive = 0
        if os.path.exists(abs_path):
            file_has_size = os.stat(abs_path).st_size
            if file_has_size < file_siza:
                # 断点续传
                self.request.sendall('800'.encode('utf8'))
                choice = self.request.recv(1024).decode('utf8')
                if choice == 'Y':
                    self.request.sendall(str(file_has_size).encode('utf8'))
                    has_receive=file_has_size
                    f=open(abs_path,'ab')

                else:
                    f = open(abs_path, 'wb')

            else:
                # 文件完全存在
                self.request.sendall('801'.encode('utf8'))
                return


        else:
            self.request.sendall('802'.encode('utf8'))
            f = open(abs_path, 'wb')

        while has_receive < file_siza:
            try:
                data = self.request.recv(1024)
            except  Exception as e :
                break

            f.write(data)
            has_receive += len(data)


        f.close()
