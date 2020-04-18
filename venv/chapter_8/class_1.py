#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 12:23
# @Author  : mr.chen
# @Site    :
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com
# list 切片
# ===================
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0])
print(l[1])
print(l[2])
# ==================
i = 0
while i < 3:
    print(l[i])
    i += 1  # i=i+1
# ==================
# 下标0到3
print(l[0:3])
# 下标1到5
print(l[1:5])
# 倒数第五个到倒数第二个
print(l[-5:-1])
# 从下标2开始切片到最后
print(l[2:])
# 每两个切一个
print(l[::2])
# 可
s = "python"
z = s[2:]
print(z)

# 可
t = (2, 12, 34, 21)
print(t[1:3])

# 不可切片 l = {1, 2, 3}  set 集合
# print(l[0:1])

# 不可切片  dict 字典
# dic = {1: 2, 3: 1, 22: 111, 3344: 222}
# print(dic[1:2])
