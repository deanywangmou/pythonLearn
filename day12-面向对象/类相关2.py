# coding=utf-8
'''
1.数据属性
2.函数属性
'''


class Chinese:
    '设计一个中国人的类'
    dang = '共产党'

    def speak():
        print('中国人都说普通话')


print(Chinese.dang)
Chinese.speak()
print(Chinese.__dict__)  # 查看属性字典
Chinese.__dict__['speak']()

print('---------------------------')

print(Chinese.__name__)  # Chinese
print(Chinese.__doc__)  # 设计一个中国人的类
print(Chinese.__base__)  # <class 'object'>
print(Chinese.__module__)  # __main__
print(Chinese.__class__)  # <class 'type'>
