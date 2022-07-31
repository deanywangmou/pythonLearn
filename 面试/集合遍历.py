"""
@Time:2021/5/11 21:15
@Author:deanywang
@File:集合遍历.py
@return:""
"""

list1=[5,5,8,6,1,5,6,6,9,7,6,5,7,5,8,1,8,4,7]

def sort_count(list):
    '''

    :param list: 元素为int型的列表
    :return: 元素按照出现次数排序（降序）
    '''
    list2 = []
    result = []
    for i in set(list):
        list2.append([list.count(i),i])
        print(list2)

    list2.sort(reverse=True)
    print(list2)

    for count,num in list2:
            result.append(num)
    return result

print(sort_count(list1))


# list1=[5,5,8,6,1,5,6,6,9,7,6,5,7,5,8,1,8,4,7]
# res={}
# for  i in set(list1):
#     res[i]=list1.count(i)
# print(res)
# res=sorted(res,key=lambda x:res[x],reverse=True)# 返回value排序的key值
# print(res)
#
#
# for  i  in set(list1):
#     print(i)
