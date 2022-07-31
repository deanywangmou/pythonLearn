"""
@Time:2021/4/123:13
@Author:deanywang
@File:request.py
@return:""
"""
import json
import jsonpath
import requests

response = requests.get('https://api.github.com')
print(type(response),response)

#返回二进制
print(type(response.content)) #<class 'bytes'>
print(response.content)
# result=json.loads(response.content)
# print(type(result),result)  #<class 'dict'>

# #返回文本格式
# print(type(response.text)) #<class 'str'>
# print(response.text)
#
# #返回字典格式
res=response.json()
print(res) #<class 'dict'>
print(type(res))
realres=jsonpath.jsonpath(res,"$.current_user_url")
print(realres)

