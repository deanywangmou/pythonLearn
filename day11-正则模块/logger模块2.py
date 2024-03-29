# coding=utf-8
import logging
logging.basicConfig(filename='access.log',
                    # filemode='w',  #只写，不追加
                    format='%(asctime)s - %(filename)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')


