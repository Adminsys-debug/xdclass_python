#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 09:30
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com

# 警告 warning
import warnings

# def my_func():
#     print("hello=======>>>>>")
#     warnings.warn("don'n use",DeprecationWarning)
#     # print(help(warnings.warn))
#
# my_func()

with open("test.txt", "w") as f:
    f.write("www.baidu.com")
    z = [12, 3, 4, 5]
    for i in z:
        f.write("\n"+str(i))
    f.close()
try:
    print(10 / 0)
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("hello world...")
