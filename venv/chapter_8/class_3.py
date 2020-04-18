#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 16:20
# @Author  : mr.chen
# @Site    :
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com

from collections.abc import Iterable

# for i in range(5):
#     print(i)
d = {"Admin_sys": "A", "Ci猿声": "公众号", "blog": "博客园"}
for i in d:
    # i为dict的keys
    print(i)
    # 如果要打印values
    print(d[i])

# 判断数据是否为可迭代对象
print(isinstance(range(1), Iterable))
# 求各子列表的和
list_ = [[1, 2, 3], [1, 33, 4]]
for x, y, z in list_:
    print("x+y+z=", x + y + z)


