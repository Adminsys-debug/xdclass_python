#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 19:18
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re

str_ = "1 2hello1 2world"
# \d提取所有为数字的字符
d_res = re.findall("\d", str_)
print(d_res)

# \D提取所有非数字的字符
D_res = re.findall("\D", str_)
print(D_res)

# 提取换页符 \f
str_f = "1 2hello1 2world" + chr(12)
f_res = re.findall("\f", str_f)
print(f_res)

# \S提取所有可见的字符
S_str = "hello world"
S_res = re.findall("\S", S_str)
print(S_res)

# \s提取所有不可见的字符
s_str = "hello world"
s_res = re.findall("\s", S_str)
print(s_res)

# \w匹配所有的单词字符
w_str = "hello world_"
w_res = re.findall("\w", w_str)
print(w_res)

# \W匹配所有的非单词字符
W_str = "hello world_"
W_res = re.findall("\W", W_str)
print(W_res)

