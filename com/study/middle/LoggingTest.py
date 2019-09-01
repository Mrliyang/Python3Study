#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : LoggingTest.py
# @Time     : 2019-09-01 13:35
# @Author   : Leon
# @Email    : 635685051@qq.com
# @Software : PyCharm
"""


import logging


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    log = Logger('myLog.log', logging.ERROR, logging.DEBUG)
    log.debug('a debug message.')
    log.info('a info message.')
    log.warning('a warning message.')
    log.error('a error message.')
    log.critical('a critical message.')
