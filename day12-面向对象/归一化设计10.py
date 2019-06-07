# coding=utf-8
import abc


# 归一化，字类必须重写父类方法，起到限制字类作用,实际就是抽象方法
class All_file(metaclass=abc.ABCMeta):
    name = ''

    @abc.abstractmethod
    def read(self):
        print(self.name + '   read')

    @abc.abstractmethod
    def write(self):
        print(self.name + '   write')


class Disk(All_file):
    name = 'Disk'


class Cdrom(All_file):
    name = 'Cdrom'


class Mem(All_file):
    name = 'Disk'

    def read(self):
        print(self.name + '   read')

    def write(self):
        print(self.name + '   write')


me = Mem()

me.read()
me.write()
