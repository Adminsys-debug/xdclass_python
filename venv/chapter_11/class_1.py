#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 11:10
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com

#
# def my_power(n):
#     return n ** 2


# print(my_power(3))
# power = lambda x: x ** 2
# print(power(2))
#
# print((lambda x: x ** 2)(5))
# power = lambda x, y: x * y
# print(power(3, 2))
# def add_(func, l=[]):
#     return [func(x) for x in l]
#
#
# print(add_(lambda x: x + 1, [1, 2, 3]))
# print(add_(lambda x: x * 2, [1, 2, 3]))

op = lambda i, n: i ** 3 + 2 + n
print(op(2, 3))
