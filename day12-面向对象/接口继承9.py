# coding=utf-8

class All_file:
    name = ''

    def read(self):
        print(self.name + '   read')

    def write(self):
        print(self.name + '   write')


class Disk(All_file):
    name = 'Disk'


class Cdrom(All_file):
    name = 'Cdrom'


class Mem(All_file):
    name = 'Disk'


ds = Disk()
cd = Cdrom()
me = Mem()

ds.read()
ds.write()
cd.read()
cd.write()
me.read()
me.write()
