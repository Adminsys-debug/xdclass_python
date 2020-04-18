#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 16:23
# @Author  : mr.chen
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        sex = "man"
        print("%d age %s is eating...... %s" % (self.age, self.name, sex))


# tagger = Animal("tagger", 18)
# # tagger.eat()
# 修改并访问类变量
# print(Animal("cat", 11).name)
# t = Animal("tagger", 18)
# print(Animal("tagger", 18))
