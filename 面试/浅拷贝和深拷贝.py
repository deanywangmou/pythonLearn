"""
@Time:2021/4/18 10:54
@Author:deanywang
@return:""
"""
import copy

#定义一个列表，其中第一个元素是可变类型。
list1 = [[1,2], 'fei', 66]
#进行浅copy
list2 = copy.copy(list1)
# list3=list1.copy()
#对象地址是否相同。
print(id(list1))
print(id(list2))
# print(id(list3))
#结果：不同
# 46177816

print('----------------------------------')
# 46177936#第一个元素地址是否相同。
print(id(list1[0]))
print(id(list2[0]))
#结果：相同
# 46240432
# 46240432


print('----------------------------------')
#第二个元素地址是否相同。
print(id(list1[1]))
print(id(list2[1]))
#结果：相同
# 45547328
# 45547328

print('----------------------------------')
#改变第一个值,查看复制对象变化。
list1[0][0] = 2
print(list2)
#结果：复制对象发生变化
# [[2, 2], 'fei', 66]
#改变第二个值,查看复制对象变化。
list1[1] = 'ge'
print(list2)
#结果：复制对象没发生变了
# [[2, 2], 'fei', 66]

