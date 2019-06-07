# coding=utf-8
import threading
import time


class MyThread(threading.Thread):
    def actionA(self):
        r_Lock.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(2)

        r_Lock.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(1)

        r_Lock.release()
        r_Lock.release()

    def actionB(self):
        r_Lock.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(2)

        r_Lock.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(1)

        r_Lock.release()
        r_Lock.release()

    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':
    r_Lock = threading.RLock()

    li = []
    for i in range(5):
        t = MyThread()
        t.start()
        li.append(t)

    for t in li:
        t.join()

    print('ending....')
