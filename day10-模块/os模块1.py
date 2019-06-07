# coding=utf-8
import os

# 1.获取当前文件的目录
print('(1)', os.getcwd())  # D:\workspace\day10-模块

# 2.改变当前的工作目录，相当shell下的cd
os.chdir("test1")
print('(2)', os.getcwd())  # D:\workspace\day10-模块\test1

# 3.回到上一级目录
os.chdir("..")
print('(3)', os.getcwd())  # D:\workspace\day10-模块

# 4.获取当前父目录字符串名
os.pardir
print('(4)', os.getcwd())  # D:\workspace\day10-模块

# 5.返回当前目录
os.curdir
print('(5)', os.getcwd())  # D:\workspace\day10-模块

# 6.可递归生成多级目录
# os.makedirs('dir1/dir2')
# print('-----------------------')

# 7.删除目录
# os.removedirs('dir1')

# 8.生成目录,相当shell中mkdir
# os.mkdir('dir3')

# 9.删除文件，相当shell中rmdir
# os.rmdir('dir3')

# 10.列出指定目录下面的所有文件
print('dir1下面的文件有', os.listdir('dir1'))

# 11.删除一个文件
# os.remove('dir1/ttttt')

# 12.文件/目录重命名
# os.rename('dir1/ttttt','dir1/mest')

# 13.获取文件/目录信息
print(os.stat('os模块1.py'))

# 14.输出操作系统特定路径，windows下为“\\”，linux下为“/”
print('输出操作系统特定路径', os.sep)

# 15.输出操作系统使用行终止符，windows下为“\r\n”，linux下为“\n”
print('输出操作系统使用行终止符', os.linesep)

# 16.输出用于分割文件路径的字符串，windows下为“；”，linux下为“：”
print("输出用于分割文件路径的字符串", os.pathsep)

# 17.输出当前平台名字,windows下为“nt”，linux下为“posix”
print("输出当前平台名字", os.name)

# 18.运行shell命令直接显示
print("运行shell命令直接显示", os.system('dir1'))

# 19.返回文件的绝对路径
print('文件的绝对路径', os.path.abspath('dir1/mest'))

# 20.返回path目录
print(os.path.split('D:\workspace\day10-模块\dir1\mest.txt'))  # ('D:\\workspace\\day10-模块\\dir1', 'mest.txt')
print(os.path.dirname('D:\workspace\day10-模块\dir1\mest.txt'))  # D:\workspace\day10-模块\dir1
print(os.path.basename('D:\workspace\day10-模块\dir1\mest.txt'))  # mest.txt

# 21.返回path目录
# BASE_DIR=os.path.dirname('dir1')
BASE_DIR = os.path.dirname((os.path.abspath('dir1')))
print('返回path目录', BASE_DIR)

# 22.如果path存在返回True，反之False
print(os.path.exists('D:\workspace\day10-模块\dir1'))  # True

# 23.如果path是绝对路径返回True，反之False
print(os.path.isabs('D:\workspace\day10-模块\dir1'))  # True

# 24.如果path是一个存在的文件则返回True，反之False
print(os.path.isfile('D:\workspace\day10-模块\dir1'))  # False,不是文件是目录

# 25.如果path是一个存在的目录则返回True，反之False
print(os.path.isdir('D:\workspace\day10-模块\dir1'))  # True

# 26.路径拼接
a = 'D:\workspace\day10-模块\dir1'
b = 'mest.txt'
print(os.path.join(a, b))  # D:\workspace\day10-模块\dir1\mest.txt

# 27.返回path所指向文件或者目录的最后存取时间
print(os.path.getatime('D:\workspace\day10-模块\dir1'))

# 28.返回path所指向文件或者目录的最后修改时间
print(os.path.getmtime('D:\workspace\day10-模块\dir1'))
