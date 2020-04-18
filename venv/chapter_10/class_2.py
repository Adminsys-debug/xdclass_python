#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 21:26
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com

# L指向一个特定的地址[1,1]
# def test(L=[]):
#     L.append("end")
#     print(L)
#
#
# # 编写默认参数时,默认参数必须指向不可变的对象,例如str,int,tuple
# test()
# test()
# lis_ = [1, 2, 3, [3, 2, 3, [32, 12, 3]]]
# for i in lis_:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for z in j:
#                     print(z)
p = (x for x in range(5))
for j in p:
    print(j)
