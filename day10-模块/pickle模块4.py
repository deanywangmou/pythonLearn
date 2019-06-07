# coding=utf-8
import pickle

dic = {'name': 'deany', 'age': 18, 'sex': 'male'}
print(type(dic))
data = pickle.dumps(dic)
print(type(data))  # <class 'bytes'>

f = open('piple文件', 'wb')
f.write(data)
f.close()

with open('piple文件', 'rb') as  f:
    t = pickle.loads(f.read())
    print(t)
    print(t['name'])
