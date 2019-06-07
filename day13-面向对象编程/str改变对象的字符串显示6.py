# coding=utf-8
class fun:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return '名字是%s,年龄是%s' % (self.name, self.age)

    def __repr__(self):
        return '这是repr'


f = fun('deany', 18)
print(f)  # str(f)--->f1.__str__()-->f.__repr__()
