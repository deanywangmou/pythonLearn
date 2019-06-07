# ！/usr/bin/env  python
# -*-  coding:utf8 -*-

f = open('deany', 'r+', encoding='utf8', newline='')  # newline读取文件中真正的换行符号

print(f.closed)  # 查看文件是否关闭 #False

print(f.encoding)  # 查看文件打开编码格式 #utf8
f.write('你好')
f.flush()  # 刷新

print(f.name)  # 读取文件名 #deany

print(f.tell())  # 光标所在位置 #6

print(f.readlines())

f.seek(3)  # 将光标移动到所选择的位置（字节）
print('tell======', f.tell())

data = f.read(4)  # 读取的是字符串
print(data)

f.truncate(10)#截取

f.close()
