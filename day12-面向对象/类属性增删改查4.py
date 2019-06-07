# coding=utf-8

class Person:
    county = 'china'

    def eat(self):
        print('%s正在吃 %s' % (self.mingzi, self.shiwu))

    def __init__(self, name, food, color):
        self.mingzi = name
        self.shiwu = food
        self.fuse = color


pp = Person('alex', '烧烤', '黄色')
pp.eat()
print(pp.county)  # china
print(Person.county)  # china


# 增加类属性
def talk(self):
    print('我们都是说普通话')


Person.speak = talk
pp.speak()
Person.age = 18
print(Person.age)

# 删除类属性
del Person.age
# print(Person.age)
print(Person.__dict__)

# 修改类属性
Person.county = '中国'
print(Person.county)


def shuohua(self):
    print('我们的语言是中文')


Person.eat = shuohua
pp.eat()

# 查看类的属性
print(Person.__dict__)

