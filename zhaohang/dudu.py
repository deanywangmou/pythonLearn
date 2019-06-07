import requests
import ssl
import urllib


header = {"content-type": "application/x-www-form-urlencoded",
           "x-requested-with": "XMLHttpRequest"
           }
session = None

def login_public(username, password, remember):
    # global session
    url = 'https://dev-env-aiforce.wezhuiyi.com/aiforce/authentication/v1/sessions'
    data = {
        "username": username,
        "password": password,
        "remember": remember
    }
    # 创建session
    session = requests.session()

# 同时打开fiddler时，对出现的ssl.SSLCertVerificationError错误进行捕获
    try:
        r = session.post(url, data, header)
    except requests.exceptions.SSLError as err:
        print(err)
        r = session.post(url, data, header, verify=False)
    return session



def login_private():
    pass


def login_out(s):
    #s = login_public('yicalltest1@wezhuiyi.com', 'abc123456', '')
    url = 'http://yicall-test.rd-bj-env.wezhuiyi.com/yicall/login/loginout?productId=119&instanceId=10511'
    r = s.get(url)
    return r

def return_session():
    global session
    return session

def set_session(s):
    global session
    session = s

# if __name__ == '__main__':
#     # 验证login_public方法
print(session)
login = login_public('yicalltest1@wezhuiyi.com', 'abc123456', '')
set_session(login)
print(session)
#     s = login_out(login)
#     print(s.text)


