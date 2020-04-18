#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 20:33
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com

# 类方法


# class Person:
#     total = 10
#
#     @classmethod
#     def print_total(cls):
#         cls.total += 1
#         print(cls.total)
#
#
# # 类名.方法名
# Person.print_total()


# 静态方法
class Person:
    i = "python"

    # 静态方法不能调用静态方法之外的变量
    @staticmethod
    def print_total():
        print("this is a staticmethod")

    def my_func(self):
        self.name = "Admin_sys"
        self.age = 27
        print(self.name, self.age)


p = Person()
p.my_func()
print(p.name)
