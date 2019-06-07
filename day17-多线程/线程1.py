# coding=utf-8
import time
import threading


def hi(num):
    print('hello %d' % num)
    time.sleep(1)


def music():
    print('begin  to  listen music :%s' % time.ctime())
    time.sleep(2)
    print('stop  to  listen music :%s' % time.ctime())


def game():
    print('begin  to  play game :%s' % time.ctime())
    time.sleep(5)
    print('stop  to  play game :%s' % time.ctime())



if __name__ == '__main__':
    # t1 = threading.Thread(target=hi, args=(10,))
    # t1.start()
    #
    # t2 = threading.Thread(target=hi, args=(5,))
    # t2.start()
    #
    # print('ending......')
    t1=threading.Thread(target=music)
    t1.start()

    t2=threading.Thread(target=game)
    t2.start()

    t1.join()
    t2.join()
    print('ending......')

