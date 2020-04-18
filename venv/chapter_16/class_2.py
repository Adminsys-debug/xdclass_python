#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 13:20
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com
from abc import ABCMeta, abstractmethod


# 抽象类
class Animal(metaclass=ABCMeta):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def activity(self):
        self.eat()
        self.run()


class Dog(Animal):
    def eat(self):
        print("eat is eating")

    def run(self):
        print("run is running")


# 实例化抽象类,一定要全部重写一边抽象类的方法,少一个方法都不行
animal = Dog()
animal.activity()
# animal.eat()
# animal.run()
