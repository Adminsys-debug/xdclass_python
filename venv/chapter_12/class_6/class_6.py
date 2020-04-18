#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 18:36
# @Author  : mr.chen
# @File    : class_6
# @Software: PyCharm
# @Email   : 794281961@qq.com
# __init__方法
# 标志所在目录是一个模块包
# 本身也是一个模块
# 可用于定于模糊导入的时候要导入的内容
# 导入包的时候,会执行__init__.py里的内容
# 可用于批量导入模块

# l = [i for i in range(1, 10000)]
# print(l)
# s_ = "student"
# # for i in s_:
# #     if i == "d" or i == "e":
# #         pass
# #     else:
# #         z = "".join(i)
# #         print(z)
# z = s_.replace("de", "")
# print(z)
#
z = []
# for i in range(1, 10000):
#     if "3" in str(i):
#         z.append(i)
# print(z)

z = [i for i in range(1, 10000) if "3" in str(i)]
print(len(z))
# print(len(z))
