"""
@Time:2021/8/16 19:12
@Author:deanywang
@File:找出列表两数之和等于目标数.py
@return:""
"""
# 7:0,
# 5:1,
# 4:2,
# -4:3,
# 2:4

def searchTarget(targe):
    searchList = [2, 4, 5, 11, 7, 13]
    searchDict = {}
    for i in range(len(searchList)):
        complete=targe-searchList[i]
        if complete in searchDict.values():
            return i,searchList.index(complete)
            # print( i,serachList[complete])
        else:
            searchDict[complete]=i


def searchTarget2(target):
    searchList = [2, 4, 5, 11, 7, 13,4,5]
    for i in range(len(searchList)):
        for j in range(i+1,len(searchList)):
            if searchList[i]+searchList[j]==target:
                # return j,i
                print(j,i)
            else:
                pass


# m=searchTarget(9)
# print(m)

m=searchTarget2(9)
# print(m)