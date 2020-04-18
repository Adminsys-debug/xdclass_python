#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 18:10
# @Author  : mr.chen
# @File    : class_8
# @Software: PyCharm
# @Email   : 794281961@qq.com

import re

# 贪婪模式 +、越多越好、一次或者多次
print(re.findall("hello+", "hellooooo"))

# 非贪婪模式 ? 0次或者一次
print(re.findall("hello?", "hellooooo"))

str_ = "<div class='news'> <div class='content'> <h3> This is a header </h3>" \
       "</div> <div class='content'> <h3> This is a heade2r</h3> </div> </div>"
# r表示原生字符串
res = re.findall(r"<div class='content'>([\s\S]*?)</div>", str_)
print(res)
