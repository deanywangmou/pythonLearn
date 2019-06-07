# coding=utf-8
class Room:
    tag = 1

    def __init__(self, name, owner, width, length, heigh):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.heigh = heigh

    @property  # 静态属性
    def cal_area(self):
        # print(self.length * self.length)
        return self.length * self.width

    # 此种方法不需要有实例
    @classmethod  # 静态方法
    def tell_info(cls):
        print(cls)
        print('>>>>', cls.tag)

    @staticmethod  # 类的工具包,statimethod不与类或对象绑定，谁都可以调用，没有自动传值效果
    def wash(name1, name2, name3):
        print('%s,%s,%s正在洗澡' % (name1, name2, name3))


r1 = Room('卧室', 'alex', 100, 100, 5)
Room.wash('name1', 'name2', 'name3')
