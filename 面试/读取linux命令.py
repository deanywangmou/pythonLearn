"""
@Time:2021/4/18 22:49
@Author:deanywang
@File:读取linux命令.py
@return:""
"""
import subprocess

# command = "ping -c 1 baidu.com "
# back = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
# print(back)
# print("back0----", back[0].decode())  # 注意需要进行解码操作，默认输出的是字节
# print("back1----", back[1].decode())  # back是一个元祖，可以通过元祖取值的方式获取结果

import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    # print(line)
    # b"'ls' \xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\xc1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n"
    # b'\xbb\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n'
    print(str(line, encoding="utf-8"))
retval = p.wait()




