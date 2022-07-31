"""
@Time:2022/1/16 19:54
@Author:deanywang
@File:math_methon.py
@return:""
"""

'''
如果接口有关联性，怎么处理

1、全局变量(缺点：关联性强，一步错步步错)
    Cookie=None
    class xxx:
        def yyy(self):
            globle  Cookie   #需要修改全局变量的值，必须声明全局变量globle

2、运用反射

    文件一 GetDate.py：
    class GetDate:
        Cookie=None  (这个属性值暂放在GetDate类中)

    文件二  TestDemo.py:
    import GetDate
    class TestDemo:
        def xxx(self):
            if res.Cookie:
                setattr(GetDate,Cookie)
3、放在SetUp()中

'''


class MathMethon:
    def  __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return  self.a+self.b

    def chengfa(self):
        return  self.a*self.b

    def chufa(self):
        return  self.a/self.b