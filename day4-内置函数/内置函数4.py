# 1.绝对值abs
print(abs(-1))  # 1

# 2.all:所有值为Tru则为True，反之只要一个为False则结果为False
print(all([1, 2, '5', 3]))  # True
print(all([1, 2, '5', 0]))  # False

# 3.any:与all相反，只要一个为True则结果为True
print(any([0, None, '', 1]))  # True
print(any([0, None, '']))  # False

# 4.bin:十进制转换成二进制
print(bin(3))  # 0b11

# 5.bool:判断bool值,空，None，0的布尔值为False，其余都为True
print(bool(''))  # False

# 6.bytes:主要用于编码和解码
name = '你好'
print(bytes(name, encoding='gbk'))
print(bytes(name, encoding='gbk').decode('gbk'))

# 7.chr:用ascii表打印出相应的符号
print(chr(97))  # a

# 8.dir:打印某一个对象中所有方法
print(dir(dict))

# 9.divmod:取商和余数，可以用来做分页功能
print(divmod(10, 3))  # (3, 1)

# 10.enumerate:将可迭代对象中的值分别取出组成一个新的可迭代对象,可以设置默认排序数
print(list(enumerate(['deany', 'hah', 3, 'sddfg '], 10)))  # [(0, 'deany'), (1, 'hah'), (2, 3), (3, 'sddfg ')]
print(set(enumerate([3, 2, 3, 7])))  # {(1, 2), (3, 7), (0, 3), (2, 3)}
test = {'name': 'xiaohong', 'age': 18}
for i, v in enumerate(test.items(), 1):
    print(i, v[0], v[1])
    # 1 name xiaohong
    # 2 age 18

# 11.eval：将字符串中的数据结构给提取出来,也可以把字符串中的表达式进行运算
dic_str = "{'name1':'deany'}"
d1 = eval(dic_str)
print(d1['name1'])  # deany

express = '1+2*3*(6/2-3)+2-5'
print(eval(express))  # -2.0

# 12.hash:可hash类型即不可变类型
print(hash('hjfgj'))

# 13.help:查看帮助
print(help(dir(all)))

# 14.hex:十进制转换成十六进制
print(hex(12))

# 15.oct:十进制转换成八进制
print(oct(12))

# 16.isinstance:判断实例类型是否正确
print(isinstance(1, int))  # True

# 17.globals:打印全局变量
car = '福特翼虎'
print(globals())
print(__file__)

# 18.locals:打印局部变量
print(locals())

# 19.max:取最大值
li = [2, 55, 88, 966, -1]
print(max(li))
print(min(li))

# 20.zip:
print('zip------------------', list(zip(('a', 'b', 'c'), (1, 2, 3))))  # [('a', 1), ('b', 2), ('c', 3)]
p = {'name': 'deany', 'age': 18, 'sex': 'man'}
print(list(zip(p.keys(), p.values())))  # [('name', 'deany'), ('age', 18), ('sex', 'man')]

# 20.max高阶:
age_dic = {'age1': 18, 'age4': 36, 'age2': 13, 'age3': 25}
print(max(age_dic.values()))  # 36
print(max(age_dic))  # 默认比较的是字典的key  #age4
print(list(zip(age_dic.values(), age_dic.keys())))  # [(18, 'age1'), (36, 'age4'), (13, 'age2'), (25, 'age3')]
print(max(zip(age_dic.values(), age_dic.keys())))  # (36, 'age4')

# 21.max终极:
people = [
    {'name': 'xiaohong', 'age': 18},
    {'name': 'deany', 'age': 33},
    {'name': 'arror', 'age': 25},
    {'name': 'zoni', 'age': 88},
]
print('>>>>>>>>>>>>>>>>>>>>>>>>', max(people, key=lambda dic: dic['age']))  # {'name': 'zoni', 'age': 88}

# 22.ord:将对应符号对应assci表编号打印出来
print(ord('a'))  # 97

# 23.pow：
print(pow(10, 2))  # 10**2  #100
print(pow(10, 2, 3))  # 100**2%3  #得到100对3取余=1

# 24.round:四舍五入
print(round(3.6))  # 4

# 25.reversed:反转
li = 'abcd'
print(list(reversed(li)))  # ['d', 'c', 'b', 'a']

# 26.set:集合
print(set('hello'))  # {'l', 'h', 'e', 'o'}

# 27.slice:切片
s = 'python'
s1 = slice(2, 5)
s2 = slice(2, 5, 2)  # 指定步长
print(s[s1])  # tho
print(s[s2])  # to

# 27.sorted：排序
people = [
    {'name': 'xiaohong', 'age': 18},
    {'name': 'deany', 'age': 33},
    {'name': 'arror', 'age': 25},
    {'name': 'zoni', 'age': 88},
]
print(sorted(people, key=lambda dic: dic['age']))

m1 = {
    'aa': 200,
    'bb': 500,
    'cc': 100,
    'dd': 2000,
}
print(sorted(m1))  # 默认按照key值排序
print(sorted(m1, key=lambda key: m1[key]))  # 返回value排序的key值
print(sorted(zip(m1.values(), m1.keys())))

# 28.sum:求和
ss = [1, 2, 3, 4, 5]
print(sum(ss))  # 15
print(sum(range(6)))  # 15


# 29.vars:
def test():
    msg = '111111111111111111112222222222222222222222222222333333333333333333333'
    print(globals())
    print(vars())


test()


