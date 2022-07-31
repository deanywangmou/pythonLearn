"""
@Time:2021/9/29 16:10
@Author:deanywang
@File:qtTool.py
@return:""
"""

from PyQt5 import  QtWidgets,QtGui
import sys

app=QtWidgets.QApplication(sys.argv)
window=QtWidgets.QWidget()
window.show()
sys.exit(app.exec_())