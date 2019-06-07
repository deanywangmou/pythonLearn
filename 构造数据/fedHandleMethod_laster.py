# coding=utf-8
import re
import time


def fedFunc():
    with  open(r'C:\Users\24368\Desktop\数据服务\fed-new', 'r', encoding='utf-8') as f1, \
            open(r'C:\Users\24368\Desktop\数据服务\laster_fed', 'w', encoding='utf-8')  as f2, \
            open(r'mySeesionIdList.txt', 'r', encoding='utf-8') as  f3:


        for  j  in  f1:
            # 找出session字段
            sessionList=re.findall('sessionId:(\w+) ',j)
            print('sessionList>>>>>>',sessionList)
            #将mySeesionIdList.txt文件中的字符取出来
            read=f3.readline()
            print(read)
            #将文件中的session替换成找出的session
            newStr=j.replace(sessionList[0],read.strip('\n'))

            # 获取当天时间
            time1 = time.strftime('%Y-%m-%d', time.localtime())
            print(time1)
            # 获取文本所有时间年月日
            timeList = re.findall('\[(\w+\-+\w+-\w+)', j)
            print('-------------------------------', timeList)
            newStr = newStr.replace(timeList[0], time1)

            f2.write(newStr)


if __name__=='__main__':
    fedFunc()