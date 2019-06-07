#!/usu/bin/env  python
# -*- coding:utf8 -*-

# 效率低1
# with open('人口普查',encoding='utf8') as f:
#     for i in f :
#         print(i,end='')

# 效率低2
# def pop():
#     ret=[]
#     with open('人口普查', encoding='utf8') as f:
#         for i in f:
#             ret.append(i)
#         return  ret
# print(pop())

def pop():
    with open('人口普查', 'r+', encoding='utf8') as f:
        for i in f:
            yield i


s = pop()
s1 = s.__next__()
s2 = s.__next__()
s3 = s.__next__()
s4 = s.__next__()
s5 = s.__next__()
print(s1, s2, s3, s4, s5)

# for k in s:
#     s1 = eval(k)
#     print(s1['population'])  # 文件返回的都是字符串

# 获取总人口信息
# all_pop = sum(int(eval(q)['population']) for q in s)
all_pop = int(eval(s1)['population']) + int(eval(s2)['population']) + \
          int(eval(s3)['population']) + int(eval(s4)['population']) + int(eval(s5)['population'])
print(all_pop)

# 获取每个省占总人数占比
print(int(eval(s1)['population']) / all_pop)
print(int(eval(s2)['population']) / all_pop)
print(int(eval(s3)['population']) / all_pop)
print(int(eval(s4)['population']) / all_pop)
print(int(eval(s5)['population']) / all_pop)
