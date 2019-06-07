# ！/usr/bin/env  python
# -*-  coding：utf-8  -*-

# 1. 打开文件，得到文件句柄并赋值给一个变量
# 2. 通过句柄对文件进行操作
# 3. 关闭文件

file = open('陈粒', 'r', encoding='utf8')
# data = file.read()
# print(data)
# 判断是否可读
print(file.readable())  # True
# 一次只会读一行
print(file.readline())
print(file.readlines())  # 所有的文本读取出来
file.close()
