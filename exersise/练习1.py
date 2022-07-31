s = "I am a good boy "
s_list = s.split()
print(s_list)
for i in range(len(s_list) - 1, -1, -1):
    print('-----',s_list[i][0])

s = "I am a boy!"
s=s.split()
s.reverse()
print(s)
result = []
for i in s:
    result.append(i[0])
print(''.join(result))

aa=[11,22,33,44,55,66,77,88,99,12,23,45]
# for  i  in range(0,len(aa),2):
#     print(aa[i])

for  j  in  range(len(aa)-1,1,-1):
    print(aa[j])