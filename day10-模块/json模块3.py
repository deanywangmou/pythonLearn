# coding=utf-8
import json

dic = {'name': 'deany'}
data = json.dumps(dic)  # 单引号会变成双引号,等同于
print(data)
print(type(data))

f_write = open('demo', 'w')
st = json.dumps(dic)  # ------->
f_write.write(st)  # ---------->等价于json.dump(dic,f_write)
f_write.close()
print('---------------------')

f_read = open('demo_new', 'r')  # --------->
data = json.loads(f_read.read())  # -------> 等价于data=json.load(f_read)
print(data)
print(type(data))
f_read.close()
