import time


# 效率低
# def producter():
#     ret = []
#     for i in range(100):
#         ret.append('包子%s' % i)
#     return ret
#
#
# def consumer(res):
#     for index, value in enumerate(res):
#         print('第%s个人，正在吃第%s个' % (index, value))
#
# res = producter()
# consumer(res)


def producter():
    c1 = consumer('wangmou')
    c2 = consumer('deany')
    c1.__next__()
    c2.__next__()
    for i in range(5):
        # time.sleep(1)
        c1.send('肉包子%i'%i)
        c2.send('菜包子%i'%i)


def consumer(name):
    print('我是[%s],我准备开始吃包子了' % name)
    while True:
        baozi = yield
        # time.sleep(1)
        print('%s很开始的将[%s]吃掉了' % (name, baozi))


producter()
