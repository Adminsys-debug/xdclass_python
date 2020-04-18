#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 13:34
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com
from functools import reduce

# reduce  驴丢死
# 把function这个函数作用到sequence序列上,最后为初始值
# reduce(function, sequence=, initial=)

# def func(x, y):
#     return x * y
#
#
# # [1,2,3,4] ===1*2*3*4=24
# print(reduce(func, [1, 2, 3, 4]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
# 初始值 先拿初始值与列表元素进行计算
print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 2))
