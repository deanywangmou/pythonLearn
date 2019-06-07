# coding=utf-8
import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('foo运行时间是%s' % (end_time - start_time))

    return wrapper


@timmer  # test=timmer(test)
def test():
    time.sleep(2)
    print('函数运行完成')


# test=timmer(test)
test()
