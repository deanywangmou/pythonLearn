"""
@Time:2021/4/17 23:21
@Author:deanywang
@File:all.py
@return:""
"""
import unittest


class GetCookie(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cookie = None

    def test_1_getCoo(self):
        GetCookie.cookie = '2133423'
        print('44444',self.cookie)

    def test_2_fun(self):
        print(self.cookie)


if __name__ == '__main__':
    unittest.main()
