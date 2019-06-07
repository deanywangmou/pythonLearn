# coding=utf-8

f=open(r'calc','r',encoding='utf8')
sum=0
for  i  in f:
    # m=len(i)
    # j=i[0:m-2]

    # j=i.strip('%\n')
    # print(j)
    # sum+=float(j)
    sum+=int(i)
print(sum)

f.close()

# import string
# aa='hellojavaee'
# dd='java'
# print(string.find(aa,dd))

