import hashlib
import requests
"""
@Time:2021/3/2811:45
@Author:deanywang
@File:interface.py
@return:""
"""

def md5EncryptTolower(password):
    # 生成一个md5对象
    m1 = hashlib.md5()
    # 使用md5对象里的update方法md5转换
    m1.update(str(password).encode("utf-8"))
    passwordMd5 = m1.hexdigest()
    return str(passwordMd5).lower()


def  test_login():
    url="https://user-do-dev.yunjiglobal.com/yunjiuserapp/userapp/verifyEncryption.json"
    headers={"Content-Type": "application/x-www-form-urlencoded"}
    appusername= "18600000003"
    apppassword= "1"
    did=appusername+apppassword
    password=md5EncryptTolower(did)
    datas={
        "loginId": appusername,
        "password": password
    }
    # datas=loginId=appusername&password=md5EncryptTolower(appusernameapppassword)
    res=requests.post(url,data=datas)
    print(res.text)
    print(res.json())
    print(res.headers)
    print(res.request.body)
    print(res.request.headers)
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        res.request.method + ' ' + res.request.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in res.request.headers.items()),
        res.request.body,
    ))

test_login()