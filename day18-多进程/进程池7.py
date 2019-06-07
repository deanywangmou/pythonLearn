# coding=utf-8
from multiprocessing import Pool
import time
import os

def Foo(i):
    time.sleep(1)
    print(i)

def Bar(args):
    print('getppid:',os.getppid())
    print('getpid:',os.getpid())

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(100):
        # pool.apply(func=Foo, args=(1,))  # 同步接口
        # pool.apply_async(func=Foo, args=(i,))#异步接口

        # 回调函数：就是某个动作或者函数执行成功后再去执行的函数
        pool.apply_async(func=Foo, args=(i,),callback=Bar)

    pool.close()
    pool.join()  # join必须要close后面

    print('end.......')
