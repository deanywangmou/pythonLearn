# ！/usr/bin/env  python
# -*-  coding：utf-8  -*-

# 开发过程中很多人回忘记写close关闭文件，为了防止忘记关闭导致操作系统被占用资源，
# 我们可以使用with关键字来帮我们管理上下文
with open('陈粒2', 'r', encoding='utf8') as  file:
    data = file.read()
    print(data)
