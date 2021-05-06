# coding=utf-8
import logging


class Logger:
    def log(self):
        logger = logging.getLogger("logger")
        logger.setLevel("DEBUG")
        fh = logging.FileHandler(filename='log.log', encoding='utf-8')  # FileHandler用来打印到文件中
        ch = logging.StreamHandler()  # StreamHandler用来打印到终端

        fm = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                               datefmt="%Y-%m-%d-%X")
        fh.setFormatter(fm)
        ch.setFormatter(fm)

        logger.addHandler(fh)
        logger.addHandler(ch)


        # logger.debug('调试debug')
        # logger.info('消息info')
        # logger.warning('警告warn')
        # logger.error('错误error')
        # logger.critical('严重critical')
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
