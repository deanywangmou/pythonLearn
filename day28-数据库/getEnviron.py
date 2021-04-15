__author__ = 'deanywang'
import logging
import os
from configparser import ConfigParser

def environ():
    pass


def configGet(path):
    con=ConfigParser()
    con.read(path)
    data_ip=con['DATABASE']['ip']
    print(data_ip)


def getFile():
    path=os.getcwd()
    path=os.path.join(os.path.dirname(path),'EVN','database.ini')
    print(path)
    return path





if  __name__=='__main__':
    getFile()
    configGet(getFile())
