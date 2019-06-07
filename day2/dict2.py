#!/usr/bin/env  python
# -*- coding:utf8  -*-

# 1.字典：以键值对存放，字典是无序的
info = {
    'test': 1,
    2: 'se',
    'k1': [
        11,
        [],
        (),
        22,
        33,
        {
            'kk1': 'vv1',
            'kk2': 'vv2',
            'kk3': (11, 22),
        }
    ],
    'sd': 2423
}

v = info['k1'][5]['kk3'][0]
print('v=', v)

for i in info.keys():  # 默认为info.keys,打印出所有的key
    print(i)
print('---------------------------')

for j in info.values():  # 打印出所有的value
    print(j)
print('************************************')

for m, n in info.items():  # 打印出所有的key值和value值
    print(m, n)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# 2.支持删除
del info['k1'][5]['kk1']
print(info)

# 3.<------------根据序列，创建字典，并指定统一的值------------->
qq = dict.fromkeys([22, 'ww', '999'], 123)
print(qq)  # {22: 123, 'ww': 123, '999': 123}

# 4.get根据key获取值，key不存在时，可以指定默认值none，也可以指定value值
dict0 = {
    'k1': 111,
    'k2': 'ada2',
    'k3': 'ada3',
    'k4': 'ada4',
    'k5': 'ada5',
    'k6': 'ada6',
}
ww = dict0.get('k1111')
print(ww)  # None
ee = dict0.get('k111', 100)
print(ee)  # 100

# 5.pop删除字典元素,并且可以获取该删除的值
vv = dict0.pop('k1')
print(dict0)  # {'k2': 'ada2', 'k3': 'ada3', 'k4': 'ada4', 'k5': 'ada5', 'k6': 'ada6'}
print(vv)  # 111
cc = dict0.pop('k1111', 10)
print(cc)  # 10,由于“k1111不存在，默认赋值10给“k1111”


# 6.删除键值对,随即删除
dict1 = {
    'k1': 111,
    'k2': 'ada2',
    'k3': 'ada3',
}
k, v = dict1.popitem()
print(dict1, k, v)  # {'k1': 111, 'k2': 'ada2'} k3 ada3

# 7.设置值，已经存在的键值对则不设置；如果不存在则设置值，并且均可以获取当前key对应的值
dict2 = {
    'k1': 111,
    'k2': 'ada2',
}
bb = dict2.setdefault('k1', 50)
print(dict2, bb)  # {'k1': 111, 'k2': 'ada2'} 111
ff = bb = dict2.setdefault('k3', 150)
print(dict2, bb)  # {'k1': 111, 'k2': 'ada2','k3':150} 150

# 8.更新字典值
dict3 = {
    'k1': 111,
    'k2': 'ada2',
}
dict3.update({'k1': 'v1', 'k8': 'v8'})
print(dict3)  # {'k1': 'v1', 'k2': 'ada2', 'k8': 'v8'}
dict3.update(k5=111, k8=888)
print(dict3)  # 意思是一个意思

tt="k1:v1|k2:v2|k3:v3|k4:v4|k5:v5"
tt1=tt.split('|')
print(tt1)
stt1=[]
for  i  in tt1:
    mm=i.split(':')
    tu=tuple(mm)
    stt1.append(tu)

print(stt1)
print(dict(stt1))