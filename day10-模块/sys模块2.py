# coding=utf-8
import sys
import time

print(sys.argv)  # 命令行参数List，第一个元素是程序本身路径

for i in range(100):
    sys.stdout.write('#')
    time.sleep(0.1)
    sys.stdout.flush()
