# coding=utf-8
a1={}
a1[1]=1
a1[2]=2
a1[3]=3
a1[4]=4
print (a1)

import time
import datetime
strToday = datetime.date.today()
print(strToday)



        # strToday的日期格式就是"%Y-%m-%d"
strOtherday = strToday + datetime.timedelta(days = -1)
print(strOtherday)

print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分


import random
import string
for _ in range(10):
    random_char = random.choice(string.ascii_letters + string.digits)
    print(random_char)