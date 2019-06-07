# coding=utf-8
str="k1:aa|k2:bb|k3:cc|k4:dd"
strList=str.split('|')
print(strList)
m=''
for  i  in strList:
    print(i)
    m+=i
print('{'+m+'}')
