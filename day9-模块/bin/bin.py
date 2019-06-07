# coding=utf-8
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#路径在day9模块,os.path.abspath(file)是文件绝对路径
sys.path.append(BASE_DIR)

from model import  main

if __name__=='__main__':
    pass