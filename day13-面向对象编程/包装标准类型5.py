# coding=utf-8
class List(list):
    def append(self, object):
        if type(object) is str:
            super().append(object)
        else:
            print("不能添加非字符串")


l = List('abcd')
l.append(123)  # 不能添加非字符串
l.append('sb')
print(l)  # ['a', 'b', 'c', 'd', 'sb']
