# coding=utf-8
# 数据描述符有__set__方法
class Type:
    def __get__(self, instance, owner):
        print('这是get方法')
        print('instance参数【%s】' % instance)
        print('owner参数【%s】' % owner)

    def __set__(self, instance, value):
        print('这是set方法')
        print('instance参数【%s】' % instance)  # instance参数【<__main__.People object at 0x02D3EE30>】
        print('value参数【%s】' % value)  # value参数【deany】

    def __delete__(self, instance):
        print('这是delete方法')
        print('instance参数【%s】' % instance)


class People:
    name = Type()

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People('deany', 26, 50000)
print(p1.name)  # None
print(p1.__dict__)
