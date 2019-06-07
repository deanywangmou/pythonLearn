# coding=utf-8
import optparse
import socketserver
from  config import  setting
from  core import server

class ArgvHandler():
    def __init__(self):
        self.op = optparse.OptionParser()
        # self.op.add_option('-s', '--server', dest='server')
        # self.op.add_option('-P', '--port', dest='port')
        options, args = self.op.parse_args()
        self.verfy_args(options, args)

    def verfy_args(self,options,args):

        cmd=args[0]
        if hasattr(self,cmd):
            func=getattr(self,cmd)
            func()


    def  start(self):
        print('服务开始运行')
        s=socketserver.ThreadingTCPServer((setting.IP,setting.PORT),server.HanderServer)
        s.serve_forever()
