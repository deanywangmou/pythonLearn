"""
@Time:2022/1/16 19:59
@Author:deanywang
@File:test_unitest_methon.py
@return:""
"""

'''
1、写用例  TestTcase
2、执行用例  1、TestSuite存储用例   2、TestLoader找用例，加载用例
3、对比实际结果
4、出具测试报告  TextTestRunner

'''

import unittest
from unittest_api.math_methon import MathMethon

class TestMathMethon(unittest.TestCase):

    def test_add_methon(self):
        res=MathMethon(1,2).add()
        print('{}+{}的结果为：'.format(1,2),res)
        self.assertEqual(res,2,msg='结果错误')

    def test_chengfa_methon(self):
        res=MathMethon(1,2).chengfa()
        print('{}*{}的结果为：'.format(1,2),res)
        self.assertEqual(res,2,msg='结果正确')

    def test_chufa_methon(self):
        res=MathMethon(1,2).chufa()
        print('{}/{}的结果为：'.format(1,2),res)
        self.assertEqual(res,2,msg='结果错误')

class TestMathMethon2(unittest.TestCase):
    def test_add_methon2(self):
        res=MathMethon(2,4).add()
        print('{}+{}的结果为：'.format(2,4),res)
        self.assertEqual(res,6,msg='结果正确')

    def test_chengfa_methon2(self):
        res=MathMethon(2,4).chengfa()
        print('{}*{}的结果为：'.format(2,4),res)
        self.assertEqual(res,4,msg='结果错误')

    def test_chufa_methon2(self):
        res=MathMethon(2,4).chufa()
        print('{}/{}的结果为：'.format(2,4),res)
        self.assertEqual(res,0.5,msg='结果错误')


if __name__ == '__main__':
    unittest.main()






