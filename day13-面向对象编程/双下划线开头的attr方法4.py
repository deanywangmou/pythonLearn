# coding=utf-8
class Foo:
    x = 1

    def __init__(self, num):
        self.num = num

    def __getattr__(self, item):
        print('执行__getattr__')

    def __delattr__(self, item):
        print('删除__delattr__')
        # self.__dict__.pop(item)

    def __setattr__(self, key, value):
        print('执行__setattr__')
        # self.key=value
        self.__dict__[key] = value


f = Foo(10)  # 实例化也是设置属性的过程
print(f.num)  # 10
f.z = 3
print(f.__dict__)
print(getattr(f, 'num'))  # 10
f.count  # 只有在属性不存在时，会自动触发__getattr__方法
print('----------------------')

# 删除属性时会触发__delattr__
del f.num  # 删除__delattr__
del f.x  # 删除__delattr__
print('----------------------', f.__dict__)  # 重写方法但是没有执行删除操作

# 设置属性时候会触发__setattr__
print(f.__dict__)
f.k = 5
print(f.__dict__)
