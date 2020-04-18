#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 14:37
# @Author  : mr.chen
# @File    : class_5
# @Software: PyCharm
# @Email   : 794281961@qq.com
# sorted(iterable,/,*,key=None,reverse=False)
# iterable为序列,默认reverse=False为升序,True时为降序

# li = [1112, 222, 212, 3434, 33, 2234]
# print(sorted(li))

data = [[1, 20], [3, 22], [222, 12]]
print(sorted(data, key=lambda item: item[0]))
