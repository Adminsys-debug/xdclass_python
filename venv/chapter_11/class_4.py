#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 14:06
# @Author  : mr.chen
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com
# filter(function,__iterable=)


def my_fun(x):
    return x % 2 == 0


# function必须返回的是布尔值,取true
res = filter(my_fun, [1, 2, 3, 4, 5])
print(type(res))
print(list(res))
