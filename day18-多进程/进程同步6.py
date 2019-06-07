# coding=utf-8
import multiprocessing


def func(l, i):
    l.acquire()
    print('hello word %s' % i)
    l.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()

    for i in range(10):
        p = multiprocessing.Process(target=func, args=(lock, i))
        p.start()
