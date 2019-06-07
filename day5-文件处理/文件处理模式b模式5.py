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
