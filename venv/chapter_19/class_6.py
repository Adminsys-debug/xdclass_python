#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 16:58
# @Author  : mr.chen
# @File    : class_6
# @Software: PyCharm
# @Email   : 794281961@qq.com

import re

# ^ 匹配整个字符串的开头

str_url = "https://xdclass.net httsssa http://www.baidu.com"
print(re.findall("^https\S*", str_url))

# $ 匹配整个字符串的结尾
print(re.findall("com$", str_url))

# \b 匹配一个单词边界
str_ = "xdclass xd123"
print(re.findall(r"\bxd", str_))
print(re.findall(r"class\b", str_))

# \B 匹配一个非单词边界
str_ = "xdclass 11xd123"
print(re.findall(r"\Bxd",str_))
