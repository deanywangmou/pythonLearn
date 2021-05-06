# coding=utf-8
import logging


class Logger:
    def log(self):
        #创建一个日志器
        logger = logging.getLogger("logger")
        #设置日志输出最低登记，低于当前等级就会被忽略
        logger.setLevel("DEBUG")
        if not logger.handlers:
            # 创建处理器
            fh = logging.FileHandler(filename='log2.log', encoding='utf-8')  # FileHandler用来打印到文件中
            ch = logging.StreamHandler()  # StreamHandler用来打印到终端

            # 创建一个格式器
            fm = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                   datefmt="%Y-%m-%d-%X")
            fh.setFormatter(fm)
            ch.setFormatter(fm)

            logger.addHandler(fh)
            logger.addHandler(ch)
        return logger

    def sum(self, a, b):
        try:
            sum = a + b
            self.log().info("{}+{}之和为{}".format(a, b, sum))
            return sum
        except Exception  as error:
            self.log().error("{}+{}计算错误{}".format(a, b, error))


Logger().sum(1, 2)
Logger().sum('m', 2)
Logger().sum('m', 55)
