"""
@Time:2021/11/18 18:56
@Author:deanywang
@File:testevn.py
@return:""
"""
import os

def getevn():
    print('os.getcwd():'+os.getcwd()+'/tttttt')
    print('os.path.relpath:'+os.path.realpath(__file__)+'/tttttt')


if __name__ == '__main__':
    getevn()