#!/usr/bin/env python 
# _*_ coding:UTF-8 _*_
"""
__title__ = ''
__author__ = 'Goode'
__mtime__ = '2018/9/12'
"""

import re
# p = re.compile(r'\d+')
# m = p.match("abcd1234efg678oo")
#
# # print(m)
# print(m.group())
#
# p = re.compile(r'([a-z]+)([a-z]+)', re.I)
# m = p.match("abcd 1234efg678oo")
#
# print(m)
# # print(m.start(0))
# # print(m.end(1))
# print(m.groups())
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
#
# print(m.groups(0))
# print(m.groups(1))
# print(m.groups(2))

# p = re.compile(r'\d+')
# m = p.search("abcd1234efg678oo")
#
# print(m)
# print(type(m))

p = re.compile(r'\d+')
m = p.match("123")

print(m)
print(type(m))

# p = re.compile(r'\d+')
# m = p.findall("abcd1234efg678oo")
#
# print(m)
# print(type(m))



# 匹配中文
# 大部分中文表示范围[u4e00-u9fa5]
# title = '你好 世界，woshixiaoxuesheng'
# p = re.compile(r'[\u4e00-\u9fa5]+')
# rst = p.findall(title)
# print(rst.)

# 爬虫中经常用第二个,默认是贪婪的匹配
title = '<div>name</div><div>age</div>'
p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')
m1 = p1.search(title)
m2 = p2.search(title)
print(m1.group())
print(m2.group())

