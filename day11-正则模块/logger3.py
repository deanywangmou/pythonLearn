# coding=utf-8
import logging

logger = logging.getLogger()
fh = logging.FileHandler('log.log')  # FileHandler用来打印到文件中
ch = logging.StreamHandler()  # StreamHandler用来打印到终端

fm = logging.Formatter("%(asctime)s %(filename)s %(message)s")
fh.setFormatter(fm)
ch.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel("DEBUG")

logger.debug('调试debug')
logger.info('消息info')
logger.warning('警告warn')
logger.error('错误error')
logger.critical('严重critical')
