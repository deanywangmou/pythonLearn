"""
@Time:2021/4/18 11:30
@Author:deanywang
@File:1~100求和.py
@return:""
"""

#1到100的和
sum=0
for  i  in range(101):
    sum+=i
print(sum)

# a=0
# num=0
# while a<101:
#     num+=a
#     a+=1
# print(num)

#编写九九乘法表
for i  in range(1,10):
    for j  in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j)+'\t',end='')
    print()



















