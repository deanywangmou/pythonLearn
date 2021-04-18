"""
@Time:2021/4/18 11:07
@Author:deanywang
@File:深拷贝.py
@return:""
"""

import copy
#定义一个列表，其中第一个元素是可变类型。
list1 = [[1,2], 'fei', 66]
#进行深copy
list2 = copy.deepcopy(list1)
#对象地址是否相同。
print(id(list1))
print(id(list2))
#结果：不同
# 46177816
# 46177936

print('----------------------------------')
#第一个元素地址是否相同。
print(id(list1[0]))
print(id(list2[0]))
#结果：不同
# 49123856
# 49588784
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
#结果：复制对象没发生变了
# [[1, 2], 'fei', 66]
#改变第二个值,查看复制对象变化。
list1[1] = 'ge'
print(list2)
#结果：复制对象没发生变了
# [[1, 2], 'fei', 66]