#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 09:54
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com
# tcp:面向连接,可靠的,基于字节流的通讯协议
# udp:无连接
import socket

i = "python"
z = i.split("thon", )
print(z)
print(len(i))
print(i[-1], "222")
if i[-1] == "n":
    z="n"
    print("i最后一个字母为 %s" % z)
