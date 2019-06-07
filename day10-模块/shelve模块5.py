# coding=utf-8
import shelve

f = shelve.open(r'shelve.txt')  # 目的：将一个字典放入一个文本
f['stu1_info1'] = {'name': 'deany', 'age': 18, 'sex': 'male'}
f['stu1_info2'] = {'name': 'deany', 'age': 18, 'sex': 'male'}
f['stu1_info3'] = {'name': 'deany', 'age': 18, 'sex': 'male'}

print(f.get('stu1_info1')['age'])
