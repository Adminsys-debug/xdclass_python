#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 17:30
# @Author  : mr.chen
# @File    : class_3
# @Software: PyCharm
# @Email   : 794281961@qq.com

# 多进程

import multiprocessing


def print_name():
    print(multiprocessing.current_process().name)


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=print_name, name="进程1")
    process2 = multiprocessing.Process(target=print_name, name="进程2")
    process1.start()
    process2.start()
