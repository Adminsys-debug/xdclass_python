#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 20:08
# @Author  : mr.chen
# @File    : class_6
# @Software: PyCharm
# @Email   : 794281961@qq.com
import time


def my_fun():
    print("这是一个测试")
    # start_ = time.time()
    # time.sleep(5)
    # end_ = time.time()
    # print(end_ - start_)


def my_time(func):
    begin = time.time()
    time.sleep(3)
    func()
    end_ = time.time()
    print(end_ - begin)


# my_fun()
my_time(my_fun)