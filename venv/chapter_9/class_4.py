#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 18:24
# @Author  : mr.chen
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com
import sys

print(sys.getrecursionlimit())


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))

# 斐波那契数列 1,1,2,3,5,8,13,21,34....
# f(1) = 1
# f(2) = 1
# f(3) = f(1) + f(2)
# f(n) = f(n - 2) + f(n - 1) n>=3

def feb(n):
    if n <= 2:
        return 1
    else:
        return feb(n - 2) + feb(n - 1)


print(feb(8))
