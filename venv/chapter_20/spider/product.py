#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:16
# @Author  : mr.chen
# @File    : product
# @Software: PyCharm
# @Email   : 794281961@qq.com


class Product:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

    def __eq__(self, o: object) -> bool:
        return self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return "产品名: %s 描述: %s 价格: %s" % (self.name, self.desc, self.price)


