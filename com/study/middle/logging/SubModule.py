#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : SubModule.py
# @Time     : 2019-09-01 15:24
# @Author   : Leon
# @Email    : 635685051@qq.com
# @Software : PyCharm
"""


import logging


logger = logging.getLogger('main.module.submodule')
logger.info('logger of submodule say something...')


def test():
    logger.info('this is submodule.test()...')
