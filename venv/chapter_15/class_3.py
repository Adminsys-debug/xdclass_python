#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 11:04
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com
# 打破访问控制


class Person:
    def __init__(self, name, age):
        self.name = name
        # 加上__表示变量私有化,不能被外界访问
        self.__age = age

    # 加上__表示方法私有化,不能被外界访问
    def __introduce_self(self):
        print(self.name, "======", self.__age)

    def setAge(self, age):
        if age <= 0 or age > 150:
            raise Exception("年龄不合法")
        self.__age = age


person = Person("Admin_sys", 11)
person.setAge(22)
print(person.__dict__)

# person.__age = 12
# 查看类中所有的变量用 __dict__
# print(person.__dict__)
# person._Person__age = 12
# print(person._Person__age)
# print(person.__dict__)
# print(person.__age)
# person.introduce_self()
