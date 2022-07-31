"""
@Time:2022/6/29 10:20
@Author:deanywang
@File:getSrtingNum.py
@return:""
"""
#
# def countStr(args):
#     strList=args.split(' ')
#     newStr=strList[-1]
#     print(len(newStr))
#
# strlen=input('请输入一个字符串')
# countStr(strlen)
#
#
# test1 ="ABCabc"
# print(test1.upper().count('A'))

#
# test='I like beijing.'
# testList=test.split(' ')
# print(testList)
# testList.reverse()
# print(testList)
# print(' '.join(testList))

# import random
# testList = []
# for i in range(3):
#     test = random.randint(1, 3)
#     testList.append(test)
# print(set(testList))
# for m in set(testList):
#     print(m)
#
# ss = 'shdsdhbsadjb\tshdahbasdj\tsfa\tasdasd\tsadas'
# n = ss.expandtabs(6)  # 断句6个，不足用\t补齐
# print(n)


'''输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。'''

# test = 'abccd2dfiush5isifhsd6fhisdhf7'
# funList = []
# nn =int( len(test )/ 8)
# print(nn)
# for i in range(nn+1):
#   funList.append(test[i*8:(i+1)*8])
#
# for j  in funList:
#     print(j.ljust(8,'0'))


mt = 180
mtList = []
for i in range(2, mt // 2 + 1):
    while mt % i == 0:
        mt = mt / i
        mtList.append(i)

# print(mtList)
# print(' '.join(mtList))


# a, res = int(input()), []
# for i in range(2, a // 2 + 1):
#     while a % i == 0:
#         a = a / i
#         res.append(i)
# print(" ".join(map(str, res)) + " " if res else str(a) + " ")



import re

test = "A 1 0 1 1150175017(&^%&$vabovbaoadd 123#$%#%#O"

a = re.findall('[A-Z]', test)
print(len(a))



# import re
test = "A 1 0 1 1150175017(&^%&$vabovbaoadd 123#$%#%#O"

# a=re.findall('[A-Z]',test)
# print(len(a))
demo = []
for i in test:
    # if i.isupper():
    #     demo.append(i)
    if ord(i) >= 65 and ord(i) <= 92:
        demo.append(i)
print(len(demo))

test1 = "This is a sample", 16
print(type(test1))
test1 = test1[0].split(',')[0]
print(test1)
para = test1.swapcase()
pp = para.split(' ')
print(pp)
pp.reverse()
print(' '.join(pp))


class Solution:
    def maxArea(self, height):
        ll = []
        height.sort(reverse=True)
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if height[i] == height[j]:
                    height.sort(reverse=True)
                    vo = height[0] * height[1]
                    if vo not in ll:
                        ll.append(vo)
                        print(ll[0])
                        # print(height)
                        # print(height[0]*height[1])


Solution().maxArea([1, 7, 3, 2, 4, 5, 8, 2, 7])


class Solution:
    def minmumNumberOfHost(self, n, startEnd):
        # write code here
        ao = startEnd
        n = 0
        for i in range(len(ao)):
            for j in range(i + 1, len(ao)):
                if ao[i][1] > ao[j][0]:
                    n += 1
                if ao[i][1] == ao[j][0]:
                    ao.pop(j)

        print(n)


Solution().minmumNumberOfHost(3, [[1, 3], [2, 4], [1, 2], [3, 4]])
