#!/user/bin/env  python
# -*- coding:utf-8 -*-
import time

'''
def cal(n):
    print(n)
    if int(n/2)==0:
        return  n
    res=cal(int(n/2))
    return  res
cal(10)
'''

person_list = ['小明', '小红', '小刚', 'deany']


def search(person_list):
    print('-' * 60)
    if (len(person_list) == 0):
        return '没人知道'
    person = person_list.pop(0)
    if person == 'deany':
        return '%s说：我知道，科兴科学园在南山' % person
    print('hi帅哥[%s],请问你知道科兴科学园在哪里吗？' % person)
    print('%s回答到：我不清楚，但念你慧眼识珠，我帮你问问%s' % (person, person_list))
    # time.sleep(1)
    res = search(person_list)
    print('%s问的结果是：%s' % (person, res))
    return res


res = search(person_list)
print(res)

