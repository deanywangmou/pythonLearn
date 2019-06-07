# coding=utf-8

import threading
import time


def sub():
    # print('ok')
    global num

    lock.acquire()
    temp = num
    time.sleep(0.01)
    num = temp - 1
    lock.release()

li = []
num = 100
lock=threading.Lock()

for i in range(100):
    print('thread:',i)
    t = threading.Thread(target=sub)
    t.start()
    li.append(t)


for t in li:
    t.join()

print(num)
