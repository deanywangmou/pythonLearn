"""
@Time:2021/5/7 21:32
@Author:deanywang
@File:字符处理.py
@return:""
"""

# str1='i love  china'
# str2='oein'
# str3=''
# for  i  in str2:
#     if i not  in str3:
#         str3+=i
#
# for  i in str3:
#     str1=str1.replace(i,"")
# print(str1)
str1='i love  china'
str2='egon'
str3=''
for i in str1:
    for j in str2:
        if j == i:
            str1 = str1.replace(j,'')
print(str1)



s = ''
for i in str1:
    if i not in str2:
        s += i
print(s)