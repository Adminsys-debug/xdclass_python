#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 16:40
# @Author  : mr.chen
# @File    : class_5
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re

# 匹配字符集

# x|y
str_o = "1a2b3c"
print(re.findall("1|2", str_o))

str_t = "110,120,189,119,1ssa"
# [] 表示取[]里面的字符,相当于占位符,
print(re.findall("1[12][09]", str_t))

# 加-、表示范围,例如[0-9]or[a-z]
print(re.findall("1[1-9][09]", str_t))

# 加^,表示取反的操作
print(re.findall("1[^0-9]+", str_t))


