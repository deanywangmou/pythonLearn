# coding=utf-8
import multiprocessing
import time
from multiprocessing import Pipe


def func(conn):
    conn.send([12, {'name': 'deany'}, 'wangmou'])
    response = conn.recv()
    print('response:', response)
    conn.close()


if __name__ == '__main__':
    parent_conn, son_conn = Pipe()

    p = multiprocessing.Process(target=func, args=(son_conn,))
    p.start()

    print(parent_conn.recv())
    parent_conn.send('儿子你好！')
    p.join()
