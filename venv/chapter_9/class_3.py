#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 18:00
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com


def my_fun():
    # return [1, 2, 3]

    # return {1,2,3}

    return 1, 2, 3


z = my_fun()
print(z[1])
# 明确有多少个返回值
i, j, l = my_fun()
print(i)
print(j)
print(l)
#  不明确有多少个返回值的情况下
result = my_fun()
print(result)
i = len(result)
for j in range(i):
    print(result[j])
