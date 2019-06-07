# coding=utf-8
tt="k1:v1|k2:v2|k3:v3|k4:v4|k5:v5"
tt1=tt.split('|')
print(tt1)
stt=[]
for  i  in tt1:
    mm=i.split(':')
    tu=tuple(mm)
    stt.append(tu)

print(stt)
print(dict(stt))
# print( dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(list(tel))  # ['jack', 'sape', 'guido']

tt=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tt)

mm={x: x**2 for x in (2, 4, 6)}
print(mm)

nn=dict(sape=4139, guido=4127, jack=4098)
print(nn)


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
   print('What is your {0}?  It is {1}.'.format(q, a))



tt = "k1:v1|k2:v2|k3:v3|k4:v4|k5:v5"
tt1 = tt.split('|')
print(tt1)
stt = []
for i in tt1:
   mm = i.split(':')
   # tu = tuple(mm)
   # stt.append(tu)
   stt.append(mm)
print(stt)
print(dict(stt))