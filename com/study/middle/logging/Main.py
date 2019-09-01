#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : Main.py
# @Time     : 2019-09-01 14:42
# @Author   : Leon
# @Email    : 635685051@qq.com
# @Software : PyCharm
"""


import logging.config
import Module


logging.config.fileConfig('conf/logging.conf')

root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')

logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'module\'...')

logger.debug('let\'s test module.testLogger()')
Module.testLogger()

root_logger.info('finish root test...')
