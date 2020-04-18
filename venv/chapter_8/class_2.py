#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 12:51
# @Author  : mr.chen
# @Site    :
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com
# print(list(range(5)))
#
# # expr for iter_var in iterable
# # expr for iter_var in iterable if cond_expr
# # 先执行iterable对象,再由普通的x循环遍历 对象,最后执行expr
# # 需求:求一个1-10 *2的列表
# range_ = [x * 2 for x in range(1, 11)]
# print(range_)
#
# # 需求:求一个1-100内的偶数列表
# # 先执行iterable对象,再由普通的x循环遍历 对象,然后执行if语句最后执行expr
# list_ = [x for x in range(1, 101) if x % 2 == 0]
# print(list_)
#
# # [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]]
# # 嵌套列表
# range_ = [[x, y] for x in range(1, 3) for y in range(6)]
# print(range_)
#
# li = [i for i in range(0, 11) if i == 7 or i == 1]
#
# print(li)
#  ------
list_ = [1, 2, 3, "31", 4, 4, 4, 3]
lia = list_[0:3]
lib = list_[4::]
lia.extend(lib)
print(lia)
z = []
# -------
# for i in list_:
#     if i == "31":
#         pass
#     else:
#         z.append(i)
# print(z)
# [z.append(i) for i in list_ if i != "31"]
# print(z)

# # 包左不包右
# print(list_[1:3])
#
# i = list(range(5))
# print(i)
#
# lq = [x for x in i if x == 3]
# print(lq)
#
# lz = [[x, y] for x in range(2) for y in range(1, 101) if y <= 50]
# print(lz.__len__())
