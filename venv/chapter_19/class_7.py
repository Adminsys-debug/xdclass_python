#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 17:21
# @Author  : mr.chen
# @File    : class_7
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re

str_ = "<h1 class='exp'>这个是我要提取的内容</h1>"

print(re.findall("<h1 class='exp'>([\S]*)</h1>", str_))
print(re.findall("<h1.*>(.*)</h1>", str_))

str_ = "<body>  <h1>标题问题内容</h1> <h3 class='abc'>我的字体大小16px,去掉加粗</h3> </body> "
print(re.findall(r"<h[1-3].*>(.*)</h[1-3].*>", str_))

# (?P<name>正则表达式) search  name为别名
result = re.search(r"<h1.*>(?P<h1>.*)</h1>[\s\S]*<h3.*>(?P<h3>.*)</h3>", str_)
print(result.group("h1"))
print(result.group("h3"))
