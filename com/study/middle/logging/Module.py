#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : Module.py
# @Time     : 2019-09-01 15:22
# @Author   : Leon
# @Email    : 635685051@qq.com
# @Software : PyCharm
"""


import logging
import SubModule


logger = logging.getLogger('main.module')
logger.info('logger of module say something...')


def testLogger():
    logger.debug('this is module.testLogger...')
    SubModule.test()
