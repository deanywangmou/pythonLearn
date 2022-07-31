"""
@Time:2021/7/18 20:14
@Author:deanywang
@File:xmindToExcel2.py
@return:""
"""

from xmindparser import xmind_to_dict
import re
import xlwt

class xmind_to_xls():
    def  xmind_cat(self,filename):
        '''
        解析xmind文件，将文件内容打印出来
        '''
        self.read=xmind_to_dict(filename)
        print(self.read)
        # return self.read

if __name__ == '__main__':
     xmind_file = "C:\\Users\\deanywang\\Desktop\\test.xmind"  # xmind文件
     xmind_to_xls().xmind_cat(xmind_file)