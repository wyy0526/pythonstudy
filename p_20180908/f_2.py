#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Goode'
__mtimes__ = '2018/9/9'
"""

# help(open)
import time
import pickle

# with open(r'test01.txt', 'r', encoding='utf-8') as f:
#     print(''.join(list(f)))
#     for line in list(f):
#         # 会多出来n个换行
#         print(list(f))

# with open(r'test01.txt', 'r', encoding='utf-8') as f:
#     strChar = f.read(3)
#     while(strChar):
#         print(strChar)
#         time.sleep(1)
#         strChar = f.read(3)
# with open(r'test01.txt', 'a', encoding='utf-8') as f:
#     f.writelines("生活你好!");
#     f.writelines("不好");

# with open(r'test01.txt', 'a', encoding='utf-8') as f:
#     # f.writelines("生活你好!");
#     # f.writelines("不好");
#     l = ["我们", "是小", "学生"]
#     f.writelines(l)

# 序列化 pickle
# age = ['1', '小学生', 'wxs']
#
# with open(r'test01.txt', 'wb') as f:
#     pickle.dump(age, f)
#
# with open(r'test01.txt', 'rb') as f:
#     a = pickle.load(f)
# print(a)

# 持久化 shelve
# 不持支多个应用并行写入，为了解决这个问题open时可以用 flag='r'
# 修改数据忘记写回，则不会自动保存，需要强制写回参数  writeback=True

import shelve

# 不仅仅创建了shv.db文件
# shv = shelve.open(r'shv.db')
# shv['one'] = 1
# shv['two'] = 2
# shv['three'] = 3
# shv.close()

# shv读取
# shv = shelve.open(r'shv.db', flag='r')
# try:
#     print(shv['one'])
#     print(shv['abcd'])
# except Exception as e:
#     print("报错了！")
# finally:
#     shv.close()

with shelve.open(r'shv.db', flag='r') as shv:
    print(shv['one'])
