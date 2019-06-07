# coding=utf-8
from multiprocessing import Process
import time
import multiprocessing

def func(q):
    print('son process',id(q))
    q.put('111')
    q.put('222')


if  __name__=='__main__':
    q=multiprocessing.Queue()
    p=Process(target=func,args=(q,))
    p.start()
    print('main  process',id(p))
    print(q.get())
    print(q.get())