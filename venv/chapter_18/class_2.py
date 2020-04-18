#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 16:46
# @Author  : mr.chen
# @File    : class_2
# @Software: PyCharm
# @Email   : 794281961@qq.com
import threading


class MyThread(threading.Thread):
    sum = 0
    lock=threading.Lock()

    def run(self):
        # 加锁
        with MyThread.lock:
        for i in range(10000000):
            MyThread.sum += 1


thread1 = MyThread()
thread2 = MyThread()
thread3 = MyThread()
thread1.start()
thread2.start()
thread3.start()

# 等待进程时间
thread1.join()
thread2.join()
thread3.join()

# 多线程环境下才会产生线程安全性问题,并发对共享变量进行修改
#
