# coding=utf-8
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#路径在day9模块
path=sys.path.append(BASE_DIR)
print(BASE_DIR)
from  model import  test
print(test.func(2,3))


