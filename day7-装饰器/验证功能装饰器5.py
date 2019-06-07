# coding=utf-8

# 缺点：每次进入页面都需要进行用户和密码验证，极不合理，需要记录用户状态
# def auth_func(func):
#     def wrapper(*args, **kwargs):
#         username = input('请输入用户名:').strip()
#         passwd = input('请输入密码:').strip()
#         if username == 'sb' and passwd == '123':
#             res = func(*args, **kwargs)
#         else:
#             print('用户名或者密码错误')
#
#     return wrapper
#
#
# @auth_func  # index=auth_func(index)
# def index():
#     print('欢迎来到京东首页')
#
#
# @auth_func  # index=auth_func(home)
# def home(name):
#     print('欢迎回家%s' % name)
#
#
# @auth_func  # index=auth_func(order)
# def order(name):
#     print('%s购物车有：%s,%s,%s' % (name, '奶茶', '妹妹', '娃娃'))
#
#
# index()
# home('deany')
# order('deany')

user_list = [
    {'name': 'alex', 'passwd': '123'},
    {'name': 'xiaoming', 'passwd': 'abc'},
    {'name': 'xiaohong', 'passwd': '1314'},
    {'name': 'xioagang', 'passwd': 'efg'}
]
current_dic = {'username': None, 'login': False}


def auth_func(func):
    def wrapper(*args, **kwargs):
        if current_dic['username'] and current_dic['login']:
            res = func(*args, **kwargs)
            return res
        username = input('请输入用户名:').strip()
        passwd = input('请输入密码:').strip()
        for user_dic in user_list:
            if user_dic['name'] == username and user_dic['passwd'] == passwd:
                current_dic['username'] = username
                current_dic['login'] = True
                res = func(*args, **kwargs)
                return res
        else:
            print('用户名或者密码错误')

    return wrapper


@auth_func  # index=auth_func(index)
def index():
    print('欢迎来到京东首页')


@auth_func  # index=auth_func(home)
def home(name):
    print('欢迎回家%s' % name)


@auth_func  # index=auth_func(order)
def order(name):
    print('%s购物车有：%s,%s,%s' % (name, '奶茶', '妹妹', '娃娃'))


index()
home('deany')
order('deany')
