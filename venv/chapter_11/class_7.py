#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 20:40
# @Author  : mr.chen
# @File    : class_7
# @Software: PyCharm
# @Email   : 794281961@qq.com
# 装饰器
import time
from functools import reduce


# def my_fun():
#     print("这是一个函数")


def print_cont(a):
    def wrapper():
        begin = time.time()
        time.sleep(2)
        a()
        end = time.time()
        print(end - begin)

    return wrapper


@print_cont
def test():
    print("这是一个装饰器")


# test()


# l = lambda o, s: s * 2 + o
# print(l(1, 2))
#
# # print(help(map))
# s = map(lambda x: x + 1, [2, 3, 2])
# print(list(s))

# sorted()
# # list str dict tuple set
# i = {1: 2, 3: 3, 2: "p"}
# print(sorted(i, reverse=True))

# filter() 把迭代对象作为入参传给func函数去,返回true的结果集
def my(x):
    return x + 2 < 6


res = filter(my, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(res))


# reduce()  迭代对象之间元素的计算 加减乘除模
def func(x, y):
    return x + y


res = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7])
print(res)

# map() lambda 每个参数都相当于一个迭代对象，有三个参数,就有三个序列对象
res = map(lambda x, y, z: x * y * z, [1, 3, 4], [2, 3, 1], [3, 42, 1])
print(list(res))

# 生成式
l = [i for i in range(5)]
print(l)

# 生成器
p = (i for i in [31, 3, 4, 53, "333"])
print(list(p))