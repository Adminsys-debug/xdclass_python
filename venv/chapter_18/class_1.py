#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 16:29
# @Author  : mr.chen
# @File    : class_1
# @Software: PyCharm
# @Email   : 794281961@qq.com
import threading


class MyThread(threading.Thread):
    def run(self):
        print("Hello world!")


# my_thread = MyThread()
# my_thread2 = MyThread()
#
# my_thread.start()
# my_thread2.start()

# def my_func():
#     print("hello world!")
#
#
# threading.Thread(target=my_func).start()
# threading.Thread(target=my_func).start()


print(threading.current_thread().name)
