#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 21:53
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com

# 可变参数


# def my_fun(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total

# def my_fun(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
#
#
# print(my_fun(1, 2, 3))
# 形参,默认参数,可变参数,命名关键字参数,关键字参数
def my_fun(name, age=27, *num, pet_name, **kwargs):
    print(name, age, num, pet_name, kwargs)


my_fun("Admin_sys", 1, 4, 5, pet_name="心心", cat="乐乐", dog="poop")
