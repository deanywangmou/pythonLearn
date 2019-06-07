#!/usr/bin/env  python
# -*- coding:utf8  -*-


i = 1
while i <= 10:
    if i == 7:
        pass
    else:
        print(i)
    i = i + 1

# 整形int
a = '123'
print(type(a), a)
b = int(a)
print(type(b), b)
print(4 // 2)  # 取商

num = 'a'
s = int(num, base=16)  # 转换成十进制
print(s)  # 10

age = 4
r = age.bit_length()  # 当前数字二进制至少用几位表示
print(r)  # 3

test = "ALex"
v = test.capitalize()  # 首字母大写
print(v)  # ALex

v1 = test.casefold()  # 首字母大写,所有的字母变小写，这个更牛逼，很多未知的对相应的变小写
print(v)  # Alex

v2 = test.lower()  # 所有的字母变小写
tt = test.islower()  # 判断是否是小写
print(v2, tt)  # alexFalse

v22 = test.upper()  # 所有的字母变大写
tt2 = test.isupper()  # 判断是否是大写
print(v22, tt2)  # ALEXFalse

v3 = test.center(20, "*")  # 设置宽度并将内容居中，*代表空白位置填充
vv1 = test.ljust(20, '*')  # 设置宽度并将内容居左，*代表空白位置填充
vv2 = test.rjust(20, '*')  # 设置宽度并将内容居右，*代表空白位置填充
print(v3, vv1, vv2)  # ********ALex********ALex********************************ALex
vv3 = test.zfill(20)  # 设置宽度并将内容居右，默认0位置填充
print(vv3)  # 0000000000000000ALex

v4 = test.count('e')  # 计算字符出现的个数，test.count('e'，5，6)代表从第5位到第6位出现字符e的次数
print(v4)  # 1

v5 = test.endswith('ex')  # True,代表以“ex”字符结尾
v6 = test.startswith('ex')  # False,代表以“ex”字符开头
print(v5)  # True

v7 = test.find('ex')  # 从开始往后找，找到第一个之后，获取其位置值，
# test.find('e'，5，6)代表从第5位到第6位之间找，-1代表未找到下·
print(v7)  # 2

wangmou = 'iam{name},age{a}'
m = wangmou.format(name='deany', a=19)  # 格式化，将一个字符中的占位符替换为指定的值
m1 = wangmou.format_map({"name": 'deany', 'a': 19})
print(m1)
# wangmou='iam{0},age{1}'
# m=wangmou.format('deany',19)#格式化，将一个字符中的占位符替换为指定的值
print(m)

m2 = test.isalnum()  # 判断是否只出现字符或者字母    #字母+汉字+数字
print(m2)  # true

ss = 'shdsdhbsadjb\tshdahbasdj\tsfa\tasdasd\tsadas'
n = ss.expandtabs(6)  # 断句6个，不足用\t补齐
print(n)  # shdsdhbsadjb      shdahbasdj  sfa   asdasd      sadas

test1 = 'sdfddf'
n1 = test1.isalpha()  # 判断是否只出现字符,包括汉字
print(n1)

test2 = "二"
n2 = test2.isdecimal()  # 判断只出现十进制数字
n3 = test2.isdigit()  # 判断只出现数字，包括②
nn = test2.isnumeric()  # 判断只出现数字,包括②甚至包括表示数字的字符也可以
print(n2, n3, nn)  # False False True

test3 = "dEaNy"
n4 = test3.swapcase()  # 大小写转换
print(n4)  # DeAnY

test4 = "sdsd_123"
n5 = test4.isidentifier()  # 判断是否是标识符（只包含字母，数字和下划线）
print(n5)  # True

test5 = "sfsd\tasdfas\n"
n6 = test5.isprintable()  # 是否存在不可显示的字符，存在false
print(n6)  # False

test6 = "sdasdv"
n7 = test6.isspace()  # 判断是否全部是空格，若“”则是True，空字符串则是False
print("n7:", n7)  # False

test7 = "Thisistitle"
n8 = test7.title()  # 把字符转换成标题
n9 = test7.istitle()  # 判断是否是标题
print(n8, n9)  # Thisistitle True

# *********************
test10 = "你是风儿我是沙"
t = ' '
n10 = t.join(test10)  # 将字符串中的每一个元素按照指定分隔符进行拼接
print(n10)  # 你 是 风 儿 我 是 沙

test11 = " deany "
n11 = test11.lstrip()  # 默认去除左边空格，包括\t和\n，test11.lstrip(“字符”)表示去除左边字符
n12 = test11.rstrip()  # 默认去除右边空格，包括\t和\n，test11.rstrip(“字符”)表示去除右边字符
n13 = test11.strip()  # 默认去两边空格，包括\t和\n，同理
print(n11)
print(n12)
print(n13)

demo = '你大风儿我是沙'
demo1 = '去你妈的风和沙'
qq = '你士大夫是收到风算法儿来了我士大夫是奇偶沙里经济'
mm = qq.maketrans(demo, demo1)  # demo的字符被demo1替换
ww = qq.translate(mm)
print(ww)
print('--------------------------------------')  # 去士你夫和收到妈算法的来了风士你夫和奇偶沙里经济

dd = 'shdcjgasasdcaduasdd'
rr = dd.partition('s')  # 用某个字符做左分割，但是只能分割成3份
we = dd.rpartition('s')  # 用某个字符做右分割，但是只能分割成3份
print(rr, we)  # ('','s','hdcjgasasdcaduasdd')('shdcjgasasdcadua','s','dd')
re = dd.split('s')  # 根据某个字符做左分割，这个字符不展示，dd.split('s'，n)分割n次
ty = dd.rsplit('s')  # 根据某个字符做右分割，这个字符不展示，dd.rsplit('s'，n)分割n次
print(re, ty)  # ['', 'hdcjga', 'a', 'dcadua', 'dd'] ['', 'hdcjga', 'a', 'dcadua', 'dd']

zz = "sndchsb\nkjsksd\nkashdkshd"
zz1 = zz.splitlines(False)  # 分割换行，只根据True和False是否保留换行符
print(zz1)  # ['sndchsb', 'kjsksd', 'kashdkshd']

print(ord('a'))
print(chr(97))

aa='a b c d e'
bb=aa.split(' ', 1)
print(bb)
bb.reverse()
print(bb)