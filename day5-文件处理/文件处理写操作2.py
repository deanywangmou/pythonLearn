# ！/usr/bin/env  python
# -*-  coding：utf-8  -*-

file = open('陈粒2', 'w', encoding='utf8')
file.write('aaaaaaaaa\n')
file.write('bbbbbbbbbbbbbb\n')
file.write('cccccc\ndddddd\neeeeeeeeeeee\n')

# 判断是否可写
print(file.writable())  # True
# 文件内容只能写字符串
file.writelines(['fff\n', 'ggggg\n'])

file.close()
