"""
@Time:2021/4/18 10:54
@Author:deanywang
@File:__init__.py.py
@return:""
"""

list = ['tom','jan','marry','coco']
list.sort()
print(list)
list.sort(key=lambda x:len(x))
print(list)