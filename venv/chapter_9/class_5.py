#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 18:51
# @Author  : mr.chen
# @File    : class_5
# @Software: PyCharm
# @Email   : 794281961@qq.com

# a,b为形参 -形式参数
# def xxx(a,b)


def my_(a, b):
    # 三目运算符  如果a>b,那就返回a,否则就返回b
    print("a的值============", a)
    print("b的值============", b)
    return a if a > b else b


print(my_(2, 3))

# # 1,3为实参
# # my_(1,3)
# print(my_(1, 3))
#
# # a=1,b=3为位置参数,指定参数值
# s = my_(a=1, b=3)
# print(s)
