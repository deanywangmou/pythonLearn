# for就是做了迭代器功能
li = [1, 2, 3, 4]
# for  i  in  li:
#     print(i)

l_iter = li.__iter__()
print(l_iter.__next__())
print(next(l_iter))  # 内置方法
print(l_iter.__next__())
print(l_iter.__next__())

# 列表解析
print(sum([i for i in range(1000)]))  # 占用内存大，机器容易卡死

# 生成器表达式:把列表推导式的[]换成()就是生成器表达式
print(sum((i for i in range(10000))))  # 几乎不占内存

egg_list=['鸡蛋%s' %i for i in range(10)]
print(egg_list)

names=['egon','alex_sb','wupeiqi','yuanhao']
names=[len(name) for name in names if not name.endswith('sb')]
print(names)