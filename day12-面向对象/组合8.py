# coding=utf-8


# class Hand:
#     pass
#
#
# class Foot:
#     pass
#
#
# class Trunk:
#     pass
#
#
# class Head:
#     pass
#
#
# class Person:
#     def __init__(self, id_num, name):
#         self.id_num = id_num,
#         self.name = name,
#         self.hand = Hand(),
#         self.foot = Foot(),
#         self.trunk = Trunk(),
#         self.head = Head()


class school:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def zhaosheng(self):
        print('%s 正在招生' % self.name)


class Course:
    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school


s1 = school('oldboy', '北京')
s2 = school('oldboy', '南京')
s3 = school('oldboy', '深圳')

c1 = Course('linux', 10000, '60d', s1)
# c2 = Course('python', 10000, '120d', s2)
# c3 = Course('java', 10000, '120d', s3)

msg = '''
1  老男孩  北京小区
2  老男孩  南京小区
3  老男孩  深圳小区
'''

print(msg)
while True:
    menu = {
        '1': s1,
        '2': s2,
        '3': s3
    }

    choice = input('选择学校>>>:')
    school_obj = menu[choice]

    name = input('课程名>>>:')
    price = input('课程费用>>>:')
    period = input('课程周期>>>:')

    new_course = Course(name, price, period, school_obj)
    print('课程【%s】属于【%s】学校' % (new_course.name, new_course.school.name))
