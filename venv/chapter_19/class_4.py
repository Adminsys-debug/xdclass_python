#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 15:41
# @Author  : mr.chen
# @File    : class_4
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re

strs_ = "hello world hell hello world helloo world hell world hel world helloppp world helloxxx world" \
        "hellxo world helwwlo world helloooooo world helolo world hellio world hellooo world"

# * : o出现的次数0次到无限次
res_s = re.findall("hello*", strs_)
print(res_s)

# + : o出现一次或者多次
res_j = re.findall("hello+", strs_)
print(res_j)

# ？: o出现零次或者一次

res_j = re.findall("hello?", strs_)
print(res_j)

# ['hello', 'hell', 'hello', 'hello', 'hell', 'hello', 'hello', 'hell', 'hello', 'hell', 'hello']

# {n} : 匹配前面的字符刚好出现n次

res_n = re.findall("hello{2}", strs_)
print(res_n)

# ['helloo', 'helloo', 'helloo']


# {n,} : 匹配前面的字符至少出现n次
res_min_n = re.findall("hello{2,}", strs_)
print(res_min_n)

# {n,m} : 匹配前面的字符出现n到m次
res_n_m = re.findall("hello{2,4}", strs_)
print(res_n_m)

# demo
# 1.找出里面所有姓李的人的名字
# 2.找出所有李白开头的人名
# "李\S*"  \S表示李字一定要可见、*表示李字后面可出现0次或无数次
s_ = "李白 张三 李四 王五 李寻欢 李白白 李骚白 李白板 李小白"
one_res = re.findall("李\S*", s_)
print(one_res)

# "李白\S*"  \S表示李白两字一定要可见、*表示李白字后面可出现0次或无数次
two_res = re.findall("李白\S*", s_)
print(two_res)
