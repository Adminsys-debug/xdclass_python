#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 13:41
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com
# 命名空间与局部变量,全局变量
cookie = 1


# 全局变量被方法重新赋值之前, 要加global进行定义该变量, 不然会报赋值前引用局部变量a
# 因为全局变量被方法修改之后, 会变成局部变量, 所以要在方法里面加上global全局关键字


def my_func():
    global cookie
    s = 1
    v = 2
    d = 2
    if cookie >= 1:
        # print(a)
        cookie = 23
    return cookie, d, v, s


def my():
    cookie = my_func()[0]
    print(cookie)


my()

# 局部命名空间的访问
# locals()

# def my_fun():
#     a = 1
#     b = 1
#     print(locals())
#
#
# my_fun()


# 全局命名空间的访问
# a = 1
# b = 2
# print(globals())


# def my_func():
#     x = 123
#     print(locals())
#     locals()["x"] = 777
#     print("x=", x)
#
#
# my_func()
# # locals 只读  globals 可读可写
# b = 2222
# print(globals())
# globals()["b"] = 666
# print("b=", b)
