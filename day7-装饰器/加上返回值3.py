# coding=utf-8
import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print('foo运行时间是%s' % (end_time - start_time))
        return res

    return wrapper


@timmer  # test=timmer(test)
def test():
    time.sleep(2)
    print('函数运行完成')
    return '这是test的返回值'


# test=timmer(test)
res = test()
print(res)
