# coding=utf-8
import  redis

# redis 取出的结果默认是字节，我们可以设定 decode_responses=True 改成字符串
r=redis.Redis(host='172.30.4.48', port=6379,db=0,decode_responses=True)
r.set('name', 'zhangsan')   #添加
print (r.get('name'))


#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='172.30.4.48', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name1', 'zhangsan')   #添加
print (r.get('name1'))   #获取


# 1.ex - 过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
m = redis.Redis(connection_pool=pool)
m.set('food', 'mutton', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
print(m.get('food'))  # mutton 取出键food对应的值








