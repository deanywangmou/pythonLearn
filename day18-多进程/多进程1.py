# coding=utf-8
from multiprocessing import Process
import time


def func(name):
    time.sleep(2)
    print('hello ', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=func, args=('deany',))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()
    print('end......')
