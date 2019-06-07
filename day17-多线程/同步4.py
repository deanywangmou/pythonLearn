# coding=utf-8
import threading
import time


class Boss(threading.Thread):
    def run(self):
        print('Boss:今晚大家都要加班到22:00')
        print(event.isSet())
        event.set()
        time.sleep(3)
        print('Boss:22:00到了可以下班了')
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print('Worker:哎！命苦啊。。。。。')
        time.sleep(1)
        event.clear()
        event.wait()
        print('Worker:干巴得！！！！！')


if __name__ == '__main__':
    event = threading.Event()
    thread = []
    for i in range(5):
        thread.append(Worker())
    thread.append(Boss())
    for t in thread:
        t.start()

    for t in thread:
        t.join()

    print('ending.....')
