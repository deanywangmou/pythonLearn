# coding=utf-8
class Room:
    tag = 1

    def __init__(self, name, owner, width, length, heigh):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.heigh = heigh

    @property  # property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
    def cal_area(self):
        print(self.length)
        return '面积是：' + str(self.length * self.width)

    # 此种方法不需要有实例
    @classmethod  # classmehtod是给类用的，即绑定到类，类在使用时会将类本身当做参数传给类方法的第一个参数
    def tell_info(cls):
        print(cls)
        print('>>>>', cls.tag)


r1 = Room('卧室', 'alex', 100, 100, 5)
r1.cal_area
print('%s住的%s面积是：%s' % (r1.owner, r1.name, r1.length * r1.width))
print(r1.cal_area)

Room.tell_info()
