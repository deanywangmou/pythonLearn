# coding=utf-8
import threading
import time
import queue
import random

q = queue.Queue()


def Product(name):
    count = 0
    while count < 10:
        print('开始制作点心。。。。。。')
        time.sleep(random.randrange(3))
        q.put(count)
        print('厨师%s 已经制作完成%s 点心' % (name, count))
        count += 1
        print('ok..............')


def Cosumer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print('顾客%s 已经吃完%s 点心' % (name, data))
        else:
            print('没有点心可吃啦，快点做好拿过来')
        count += 1


if __name__ == '__main__':
    p1 = threading.Thread(target=Product, args=('A君',))
    c1 = threading.Thread(target=Cosumer, args=('B君',))
    c2 = threading.Thread(target=Cosumer, args=('C君',))

    p1.start()
    c1.start()
    c2.start()

    p1.join()
    c1.join()
    c2.join()

    print('就餐结束。。。。。。')
