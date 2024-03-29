# coding=utf-8
import time
import datetime

# 1.时间戳
print('时间戳是：', time.time())
# 2.结构化时间--当地时间
print('结构树时间是：', time.localtime())
t = time.localtime()
print(t.tm_year)
print(t.tm_wday)

print(time.gmtime())  # 结构化时间，gmtime是把日期和时间转换为格林威治(GMT)时间的函数

print('将时间戳转换成结构化时间',time.localtime(23456745))  # 将时间戳转换成结构化时间
print('--------------------------')

print('将结构化时间转换成时间戳',time.mktime(time.localtime(34534)))  # 将结构化时间转换成时间戳

print('--------------------------')

print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 将结构化时间转换成字符串时间strftime
# strWeekNum = time.strftime("%m", time.localtime())
# print(strWeekNum)


print('strptime:',time.strptime("2018:10:23:20:29:39", "%Y:%m:%d:%X"))  # 将字符串时间转换成结构化时间strptime
print(time.asctime())  # 结构化时间转化成字符串时间
print(time.ctime())  # 时间戳转化成字符串时间

print('--------------------------')
print(datetime.datetime.now())  # 返回当前时间
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换

strToday = datetime.date.today()
print(strToday)
print('---------*******-------')


def doCutHorizontalLine(strData):
    # 用来将日期中存在的'-'删除,返回一个没有'-'的日期字符串
    # strData: 存在’-‘的日期字符串

    listNewStrData = []
    listStrData = list(strData)
    for listStrDataItem in listStrData:
        if (listStrDataItem == '-'):
            pass
        else:
            listNewStrData.append(listStrDataItem)
    return ''.join(listNewStrData)
print(doCutHorizontalLine("2019-02-05"))


def getWeekNum():
    # 获取当前是星期几
    # add in 2018-04-02
    strWeekNum = time.strftime("%w", time.localtime())
    return strWeekNum
print(getWeekNum())



