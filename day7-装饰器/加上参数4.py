# coding=utf-8
import time


def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        print('foo运行时间是%s' % (end_time - start_time))
        return f

    return wrapper


@timmer  # test1=timmer(test1)
def test1(name, age):
    time.sleep(2)
    print('函数运行完成')
    print(name, age)
    return '这是test的返回值'


@timmer  # test2=timmer(test2)
def test2(name, age, sex):
    time.sleep(2)
    print('函数运行完成')
    print(name, age, sex)
    return '这是test的返回值'


res1 = test1('deany', 18)
print(res1)

print('------------------------------')
res2 = test2('wangmou', 20, sex='男')
print(res2)
