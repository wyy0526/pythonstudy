#!/usr/bin/env python 
# _*_ coding:UTF-8 _*_
"""
__title__ = ''
__author__ = 'Goode'
__mtime__ = '2018/9/9'
"""
# color = ['red', 'yellow', 'blue', 'green']
#
# for green in color:
#     if green == 'green':
#     # if green.__eq__('green') :
#         print("Green")

import logging

LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"

logging.basicConfig(filename='./log.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")

logging.log(logging.DEBUG, "this is a debug log")
logging.log(logging.INFO, "this is a info log")
logging.log(logging.WARNING, "this is a warning log")
logging.log(logging.ERROR, "this is a error log")
logging.log(logging.CRITICAL, "this is a critical log")