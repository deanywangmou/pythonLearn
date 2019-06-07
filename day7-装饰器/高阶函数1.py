import time


# 高阶函数定义：
# 1.函数接收的参数是一个函数
# 2.函数的返回值是一个函数名
# 3.满足上述条件任意一个，都可以称之为高阶函数

def foo():
    print('from to  foo')


def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('foo运行时间是%s' % (end_time - start_time))
    return foo


foo = timer(foo)
foo()
