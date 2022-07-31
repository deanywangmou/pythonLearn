"""
@Time:2022/1/9 15:25
@Author:deanywang
@File:日志学习.py
@return:""
"""

"""
logging模块
0、日志收集器
1、日志级别(Level)：  DEBUG、INFO、warning、error、critacal
2、输出渠道(Handle)： 控制台(StreamHandle)、终端文件(FileHandle)
3、日志内容(Format)： 时间-文件名字-报错代码行数-输出内容

logging模块，默认root日志收集器，默认输出级别：warning
1、创建一个日志收集器:logger=logging.getLogger("收集器名字")
2、给日志手机器，设置日志级别(logger.setLevel(logging.INFO)
3、设置日志输出渠道
4、设置日志输出格式
5、将日志格式帮到渠道中
6、将设置好的渠道，添加到日志收集器中
"""

import logging
from python_common_lib.my_logger import mylog
# 1、创建一个日志收集器:logger=logging.getLogger("收集器名字")
logger=logging.getLogger("log")

# 2、给日志收集器，设置日志级别(logger.setLevel(logging.INFO)
logger.setLevel(logging.INFO)

# 3、设置日志输出渠道
handle1=logging.StreamHandler()
handle2=logging.FileHandler("log.log",encoding='utf-8')

# 4、设置日志输出格式
fmt='%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行 %(message)s '
formatter=logging.Formatter(fmt)

# 5、将日志格式设置到渠道中
handle1.setFormatter(formatter)
handle2.setFormatter(formatter)

# 6、将设置好的渠道，添加到日志收集器中
logger.addHandler(handle1)
logger.addHandler(handle2)

logger.info("这是info")
mylog.info("这是框架封装好的日志对象")















