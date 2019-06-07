# coding=utf-8
import re
import time


def genFunc():
    # num_list = []
    with  open(r'C:\Users\24368\Desktop\数据服务\gen-new', 'r', encoding='utf-8') as f1, \
            open(r'C:\Users\24368\Desktop\数据服务\laster_gen', 'w', encoding='utf-8')  as f2, \
            open(r'mySeesionIdList.txt', 'w', encoding='utf-8') as f3:
        for i in f1:
            # 找出sessionid字段
            sessionIdList = re.findall('session:(\w+) ', i)
            print('sessionIdList>>>>>', sessionIdList)

            # 获取sessionid，并处理sessionid
            sessionStr = sessionIdList[0]
            print('sessionStr>>>>>', sessionStr)
            sessionList = sessionStr.rsplit('_', 1)
            print('sessionList>>>>>', sessionList)
            handerStr = sessionList[1][:-7]
            print('截取字符字符长度到倒数第7位的字符', handerStr)

            # 获取当前时间戳bong截取小数点后7位
            timer = time.time()
            time.sleep(0.1)
            print('时间戳：', timer)
            timeStr = str(timer).split('.')[1]
            print(timeStr)
            while True:
                if len(timeStr) != 7:
                    timeStr = timeStr + '0'
                else:
                    break

            # 将时间戳存入到数组
            # num_list.append(timeStr)
            newStr = handerStr + timeStr
            print('拼接后的字符', newStr)

            # 将sessionId重新组装成字符串
            newSessionContent = sessionList[0] + '_' + newStr
            # 将新生成的sessionId存入到文件中
            f3.write(newSessionContent + '\n')
            # 将文本中旧的sessionid替换成新的sessionid
            newContent = i.replace(sessionStr, newSessionContent)

            # 获取当天时间
            time1 = time.strftime('%Y-%m-%d', time.localtime())
            print(time1)
            # 获取文本所有时间年月日
            timeList=re.findall('\[(\w+\-+\w+-\w+)',i)
            print('-------------------------------',timeList)
            newContent=newContent.replace(timeList[0],time1)
            f2.write(newContent)

if __name__=='__main__':
    genFunc()

# import time

# localtime=time.localtime()
# time=localtime.tm_year
# time = time.strftime('%Y-%m-%d ', time.localtime())
# print(time)
