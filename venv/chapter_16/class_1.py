#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 11:22
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com
# 继承

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         print(self.name + "  is walking")
#
#
# class Dog(Animal):
#     def bark(self):
#         print(self.name + "is bark")
#
#
# class Cat(Animal):
#     pass
#
#
# dog = Dog("Admin_sys")
# # 判断实例是不是属于父类
# print(isinstance(dog, Animal))
# dog.walk()
# dog.bark()


class Animal:
    def __init__(self, name):
        print("Animal" + name)

    def eat(self, name):
        print(name + "is eating")


class Dog(Animal):
    # 子类同名的初始化方法及实例方法会覆盖父类的初始化方法===>>可用于重写父类方法
    def __init__(self):
        # 调用父类的构造函数
        # Animal.__init__(self, "tagger")
        # 调用父类的变量/函数,建议用super方法
        super(Dog, self).__init__("tagger")
        print("dog")

    def eat(self, name):
        print(name + "   dog is eating")


#
dog = Dog()
print(dog.__dict__)
# dog.eat("dog")
# print()
