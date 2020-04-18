#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 22:27
# @Author  : mr.chen
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com


# from enum import Enum, unique
#
#
# # 加上unique装饰器确保枚举类中的枚举成员值唯一
# @unique  # U ni ke
# # 枚举类,变量全部要大写
# class TrafficLight(Enum):  # en 按
#     # 1为红灯,2为黄灯,3为绿灯
#     # 枚举成员, RED 名字  1 值
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#
# def judge(color):
#     if color == TrafficLight.RED or color == TrafficLight.YELLOW:
#         print("司机违规")
#     else:
#         print("司机正常行驶")
#
#
# judge(TrafficLight.YELLOW)
# # 获取枚举成员名称
# print(TrafficLight.YELLOW.name)
# # 获取枚举成员的值
# print(TrafficLight.YELLOW.value)
#
# # 枚举成员值比较判断
# print(TrafficLight.YELLOW.value == 1)
#
# p = [1, 3, 2, 3, 2]
# # print(p[0:3])
# print([i for i in p if i != 3])
#
# # while i > 2:
# #     print("sss")
# #     continue
#
# p = ["python", "java"]
# i = list(range(5))
# z = map(lambda x: x + 1, i)
# print(list(z))
# res = map(lambda x: x + 1, [1, 2, 3])
# print(list(res))
#
#
# # filter(function,__iterable=)
# def my_fun(x):
#     return x % 2 == 0
#
#
# # function必须返回的是布尔值,取true
# res = filter(my_fun, [1, 2, 3, 4, 5])
# print(type(res))
# print(list(res))
#
#
# class Person:
#     i = "python"
#
#     # 静态方法不能调用静态方法之外的变量
#     @staticmethod  # si dei ke
#     def print_total():
#         print("this is a staticmethod")
#
#     def func(self):
#         self.name = 1111
#
#
# # person = Person()
# # person.print_total()
# # # 先要实例化方法,才能调用实例变量
# # person.func()
# # print(person.name)
# list_ = [11, 2, 12, 333, 3331, 33, 1]
# # len_ = len(list_)
# # print(len_)
# #
# # for i in range(0, len_):
# #     for j in range(i + 1, len_):
# #         if list_[i] > list_[j]:
# #             list_[i], list_[j] = list_[j], list_[i]
# # print(list_)
# len_ = len(list_)
#
# for i in range(0, len_):
#     for j in range(i + 1, len_):
#         if list_[i] > list_[j]:
#             list_[i], list_[j] = list_[j], list_[i]
# print(list_)

o = {1: 2, 2: "3"}
# # z = input(int())
# print(type(o))
# # print(o.values())
# z = int(input())
# # print(type(z))
# print(o.get(z))

print(o.get(int(input())))
