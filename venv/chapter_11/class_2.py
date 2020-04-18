#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 13:11
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com

# map(func, *iterable)


def add_(x):
    return x + 1


# map 把可迭代对象的元素遍历进方法里面
# res = map(add_, [1, 2, 3])
# print(list(res))

# list dict set tuple  均为可迭代对象
res = map(lambda x: x + 1, [1, 2, 3])
print(list(res))

# 利用map进行两列表求和
# map表达式：map(lambda 参数a,b,c.....: a+b+c+......,迭代对象)
res = map(lambda x, y: x + y, [1, 2, 3], [3, 2, 14])
print(list(res))
