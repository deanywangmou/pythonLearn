# coding=utf-8
import threading
import time
import queue  # 线程队列

q = queue.Queue()  # 先进先出
# q = queue.LifoQueue()  # 后进先出
# q = queue.PriorityQueue()  # 优先级
q.put(12)
q.put('hello')
q.put({'name': 'deany'})
print(q.qsize())
print(q.empty())
print(q.get_nowait())  # 相当q.get(block=False)
# q.task_done()  # 在完成一项工作之后，q.task_done()函数向任务完成的队列发送一个信号
# q.join()  # 实际上意味着队列为空在执行别的操作

while True:
    data = q.get()
    print(data)
    print('>>>>>>>>>>>')



