#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 15:34
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com

# 多态特性和构造函数


class Person:
    # 构造函数
    def __init__(self, name, age, height):
        print("这是一个初始化操作")
        self.name = name
        self.age = age
        self.height = height

    def introduce_self(self):
        print("hello,my name is %s and my age is %d and i.m %d height" % (self.name, self.age, self.height))


person = Person("Admin_sys", 27, 172)
person2 = Person("Admin_sys", 28, 173)
person.introduce_self()
person2.introduce_self()
