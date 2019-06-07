# coding=utf-8
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(0.5)
            semaphore.release()


if __name__ == '__main__':
    semaphore = threading.Semaphore(5)

    thrs = []
    for i in range(100):
        thrs.append(MyThread())

    for t in thrs:
        t.start()

    for i in thrs:
        t.join()

    print('ending.....')


