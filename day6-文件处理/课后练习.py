# 根据范围获取其中能被3和7整除的所有数之和，bong返回调用者
# 返回符合条件的数字个数以及符合条件的数字之和，如def(start,end)
# def func(start, end, num=0, sum=0):
#     if end == start:
#         return num, sum
#     if start % 3 == 0 and start % 7 == 0:
#         num += 1
#         sum += start
#     ret = func(start + 1, end, num, sum)
#     return ret
#
#
# f = func(1, 43)
# print(f)

def func(start, end, num=0, sum=0):
    for m in range(start, end + 1):
        if m % 3 == 0 and m % 7 == 0:
            num += 1
            sum += m
    return num, sum


f = func(1, 22)
print(f)

# 2.使用set集合获取两个列表l1=[11,22,33]和l2=[22,33,44]中相同的元素
l1 = [11, 22, 33]
l2 = [22, 33, 44]
s1 = set(l1)
s2 = set(l2)
ss = s1 & s2  # 求交集
print(ss)

# 3.定义函数统计一个字符大写字母、小写字母、数字的个数，并以字典为结果返回给调用者
s3 = 'asJF23@HKjg8938GDSK'
li = list(s3)

print(li)
x = y = z = 0
for m in li:
    print(type(m))
    if m.isalpha():
        if m.isupper():
            x += 1
        else:
            y += 1
    elif m.isdigit():
        z += 1
dic = {'大写': x, '小写': y, '数字': z}
print(dic)


def func(arg):
    arg.append(55)


li = [11, 22, 33, 44]
func(li)
print(li)  # [11, 22, 33, 44, 55]
li = func(li)
print(li)  # None

print('------------------------------------------------------')


def f1(arg):
    print(arg + 100)  # 108


def f2(arg):
    ret = f1(arg + 1)
    print(arg)  # 7
    print(ret)  # None


ret = f2(7)
print(ret)  # None
print('------------------------------------------------------')

# 使用zip方法实现以下功能,请获取字符串s='SB is good gay'
li1 = ['SB', 22, 33, 44]
li2 = ['is', 22, 33, 44, 55]
li3 = ['good', 22, 33, 44, 55, 66]
li4 = ['gay', 22, 33, 11]
li = list(zip(li1, li2, li3, li4))[0]
print(li)
print('_'.join(li))  # SB_is_good_gay

