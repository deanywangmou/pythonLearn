"""
@Time:2022/1/16 20:46
@Author:deanywang
@File:testSuits.py
@return:""
"""

import unittest
from unittest_api.test_unitest_methon import TestMathMethon
import HTMLTestRunnerCN #可以直接调用
import HTMLTestRunnerNew #可以直接调用

suite=unittest.TestSuite()#存储用例

# 方法一，只执行一条用例，具体到类名
# suite.addTest(TestMathMethon('test_chengfa_methon'))
# suite.addTest(TestMathMethon('test_add_methon'))

# 方法二:Testloader,创建一个加载器
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethon))

from unittest_api import test_unitest_methon  #具体到模块
suite.addTest(loader.loadTestsFromModule(test_unitest_methon))


# 执行  上下文管理器——原始
# with open('test.txt','w+',encoding='utf-8') as fs:
#     runner=unittest.TextTestRunner(stream=fs, verbosity=2)#verbosity=0 1 2 ，为2的时候最详细
#     runner.run(suite)

#新鲜玩法html
with open('test_resport.html','wb') as fs:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=fs,
                                            verbosity=2,
                                            title='unittest单元测试报告',
                                            description='模糊学习报告')
    runner.run(suite)