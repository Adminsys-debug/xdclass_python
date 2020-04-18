#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 09:46
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com


class MyException(Exception):
    def __init__(self, parameter):
        err = "非法入参{0},分母不能为0".format(parameter)
        Exception.__init__(self, err)
        self.parameter = parameter


def my_func(x):
    if x == 0:
        raise MyException(x)
    else:
        print(10 / x)
