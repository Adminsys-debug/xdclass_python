#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:18
# @Author  : mr.chen
# @File    : test
# @Software: PyCharm
# @Email   : 794281961@qq.com

from unittest import TestCase
from class_4 import MyTest
import unittest


class TestMyTest(TestCase):
    def test_add(self):
        test = MyTest()
        self.assertEqual(test.my_add(1, 5), 6)


if __name__ == '__main__':
    unittest.main()
