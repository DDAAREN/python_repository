#!/usr/bin/env python
#!_*_ coding:UTF-8 _*_

__author__ = 'pt'

"""
    改变标准输出位置，使print的结果导入到指定的文件中
"""

import sys


def print_page(path='/tmp/.page.html'):
    __stdout = sys.stdout
    sys.stdout = open(path, 'w+')
    # print any thing
    sys.stdout = __stdout