# coding=utf-8
# 数据描述符有__set__方法
class Type:
    def __init__(self, key, expect):
        self.key = key
        self.expect = expect

    def __get__(self, instance, owner):
        print('这是get方法')
        if instance is None:
            return self
        # print('instance参数【%s】' % instance)
        # print('owner参数【%s】' % owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('这是set方法')
        # print('instance参数【%s】' % instance)  # instance参数【<__main__.People object at 0x02D3EE30>】
        # print('value参数【%s】' % value)  # value参数【deany】
        if not isinstance(value, self.expect):
            raise TypeError('%s 传的类型不是%s  ' % (self.key, self.expect))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('这是delete方法')
        # print('instance参数【%s】' % instance)
        instance.__dict__.pop(self.key)


def func(**kwargs):
    def wrapper(obj):
        for key, val in kwargs.items():
            setattr(obj, key, Type(key,val))
        return obj
    return wrapper


@func(name=str,age=int,salary=float,sex=str)
class People:
    # name = Type('name', str)
    # age = Type('age', int)

    def __init__(self, name, age, salary, sex):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People('deany', '26', 50000.2,'man')
# print(p1.name)  # deany
print(p1.__dict__)
