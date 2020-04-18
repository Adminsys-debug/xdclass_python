#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 14:23
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com
'''

class Father:
    def power(self):
        print("拥有很大的力气")

    def sing(self):
        print("Father sing")


class Mather:
    def sing(self):
        print("唱歌")


# 当继承多个父类时,不同父类有多个同名的方法,优先使用先被继承的父类的方法
class Me(Mather, Father):
    pass


me = Me()
me.power()
me.sing()
'''
# 冒泡
li = [122, 31, 33, 22]
len_ = len(li)

for i in range(0, len_):
    for j in range(i + 1, len_):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

print(li)
