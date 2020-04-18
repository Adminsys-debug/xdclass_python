#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 10:47
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com
# 访问控制


class Person:
    def __init__(self, name, age):
        self.name = name
        # 加上__表示变量私有化,不能被外界访问
        self.__age = age

    # 加上__表示方法私有化,不能被外界访问
    def __introduce_self(self):
        print(self.name, "======", self.__age)

    def setage(self, age):
        if age <= 0 or age > 150:
            raise Exception("年龄不合法")
        self.__age = age


person = Person("Admin_sys", 11)
person.__age = 12
print(person.__age)
person.introduce_self()
