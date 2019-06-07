# coding=utf-8
'''
1.数据属性
2.函数属性
'''


class Chinese:
    '设计一个中国人的类'
    dang = '共产党'

    def speak(self):
        print('中国人都说普通话')

    def action(self):
        print('%s是中国人，他也非常爱国' % self.mingzi)

    # def __init__(name,sex,age):
    #     dic1={
    #         'name':name,
    #         'sex':sex,
    #         'age':age
    #     }
    # return dic1

    def __init__(self, name, sex, age):
        self.mingzi = name
        self.xingbie = sex
        self.nianji = age


p1 = Chinese('deany', 'male', 18)  # 实例化
print('p1:', p1.__dict__)
print('Chinese:', Chinese.__dict__)
print(Chinese.dang)
Chinese.speak(p1)
Chinese.action(p1)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
p1.action()




