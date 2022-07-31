"""
@Time:2022/1/9 20:35
@Author:deanywang
@File:My_logger.py
@return:""
"""
import logging
from python_common_lib.config_read import conf

class MyLogger(logging.Logger):
    def __init__(self, name, level="INFO", file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(name, level)

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        # super().__init__(conf.get("log","level"),conf.get("log","name"))
        super().__init__(conf.get("log","name"),conf.get("log","level"))



        # 日止格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行 %(message)s '
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            handle2 = logging.FileHandler(file, encoding='utf-8')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

#是否需要写入日志文件
if conf.getboolean("log","file_write"):
    file_name=conf.get("log","file_name")
else:
    file_name=None

# file_name=conf.get("log","file_name")
# mylog = MyLogger(conf.get("log","name"), file=conf.get("log","file_name"))
mylog = MyLogger(file_name)


# if __name__ == '__main__':
#     mylog = MyLogger("日志封装", file="mylog.log")
#     mylog.info("________")
