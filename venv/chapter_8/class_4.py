#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 17:04
# @Author  : mr.chen
# @Site    :
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com
# (expr for iter_var in iterable)
# (expr for iter_var in iterable if cond_expr)
g = (i for i in range(1, 11))
# print(next(g))
# for j in g:
#     print(j)
# 利用生成式求各子列表的和  res
l = [[1, 2, 3], [2, 1, 3], [4, 3, 5], [1, 211, 12], [3996, 44, 33]]
res = [x + y + z for x, y, z in l]
print(res)
# 先定义一个int 0, 遍历res,求出该列表的总和
s = 0
for i in res:
    s = s + i
print(s)

# print(res)
