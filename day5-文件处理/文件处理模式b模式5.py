# ！/usr/bin/env  python
# -*-  coding：utf-8  -*-
# b的方式不能指定编码
file = open('陈粒', 'rb')
data = file.read()
print(data)
print(data.decode('utf8'))
file.close()

file_w = open('test.txt', 'wb')
file_w.write('123245\n'.encode('utf8'))
file_w.write(bytes('你好\n', encoding='utf8'))

m = 13500102 % 512
print(m)

from functools import reduce
# from functools import map
def fn(x, y):
    return x * 10 + y


s = reduce(fn, [1, 3, 5, 7, 9])
print((s))
