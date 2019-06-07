import requests
import json

# r = requests.get('https://www.bilibili.com')
# # 返回状态码
# print(r.status_code)  # 200
# # print(r.json())
#
# # 为了防止打印出来的结果乱码，先用utf8编码
# r.encoding = 'utf8'
# # print(r.text)#响应内容的字符串形式
#
# print(type(r))  # <class 'requests.models.Response'>
# print('打印头信息', r.headers)
#
# print(r.encoding)  # 从http消息投猜测内容编码方式
# print(r.apparent_encoding)  # 从内容分析出响应内容编码方式
# print('action....',r.content)  # http响应内容的二进制形式
#
# # print(r.cookies)#获取返回cooklie
#
# print(r.url)#获取url
# print(r.request.headers )
#
#
# stt='abcdaaabbbccsssaakhdfksdfzzaassdsdsdfdsd'
# print('aa' in  stt)
# print(stt.count('aaa'))






#
import time
#
# t1=time.time()
# print(t1)
#
t2=time.strptime("2019:04:04:20:29:39", "%Y:%m:%d:%X")
print('>>>>>>>>>>>>>>>>>>>>>>>>>',t2)
# t3=time.mktime(t2)
# print(t3)
#
# ttt=time.gmtime()
# print(time.asctime(ttt))
# print(time.ctime(t1))


data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response)
print(response.text)
print(response.json())
print(json.loads(response.text))

import random
ss=random.choice((11,22))
print(ss)

import time
rr=time.strftime('%Y%m%d%x',time.localtime())
print(rr)


import sys
print(len(sys.argv))
print((sys.argv))