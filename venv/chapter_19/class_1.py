#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 18:06
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re

# pattern, string, flags=0
# pattern 正则表达式
# string 要匹配的字符串
# flags  标志位,用于控制正则表达式的匹配方式
# re.L 做本地化识别
# re.M 多行匹配
# re.S 使,匹配包括换行在内的所有字符
# re.I 忽略大小写
# re.U 根据unicode字符集解析字符

# findall_str = "hello,my name is xdclass"
# # 泛匹配文本
# findall_res = re.findall("xdclass", findall_str)
# print(findall_res)
# # 尝试在字符串的起始位置匹配给定正则,如果不是起始位置匹配成功的化,match就返回None
# match_str = "hello world"
# match_res = re.match("hello", match_str)
# print(match_res)
# # 通过group或者groups获取具体下标值
# print(match_res.group(0))

# 扫描整个字符串并返回第一个成功的匹配
search_str = "hello hello world,hello"
search_res = re.search("hello", search_str)
print(search_res)
# 通过group或者groups获取具体下标值
print(search_res.group())