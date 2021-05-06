"""
@Time:2021/4/20 22:31
@Author:deanywang
@File:ttt.py
@return:""
"""


import requests

url="http://httpbin.org/post"
headers={"Content-Type": "application/json;charset=UTF-8"}
data={"key":"value"}

res=requests.post(url=url,headers=headers,json=data)
print(res.json()['origin'])