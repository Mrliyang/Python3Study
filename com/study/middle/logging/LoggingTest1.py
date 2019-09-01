#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : LoggingTest1.py
# @Time     : 2019-09-01 15:41
# @Author   : Leon
# @Email    : 635685051@qq.com
# @Software : PyCharm
"""


import logging


logging.basicConfig(filename='myLog1.log', level=logging.DEBUG)

# create logger
logger_name = "main_logger"
logger = logging.getLogger(logger_name)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
