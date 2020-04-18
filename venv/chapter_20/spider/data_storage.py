#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:17
# @Author  : mr.chen
# @File    : data_storage
# @Software: PyCharm
# @Email   : 794281961@qq.com

from product import Product


# 数据存储器
class DataStorage:
    def storage(self, products):
        """
        数据存储
        :param products:set结构
        :return:
        """
        for i in products:
            print(i)
