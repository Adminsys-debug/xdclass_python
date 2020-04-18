#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 09:57
# @Author  : mr.chen
# @File    : udp_server
# @Software: PyCharm
# @Email   : 794281961@qq.com

import socket

# socket.SOCK_STREAM  # tcp
# socket.SOCK_DGRAM  # udp

# UNIX只能在本机通信
socket.AF_UNIX
# INET可以跨主机
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 8888))
print("UDP 服务端已经启动")

while True:
    data, client = server.recvfrom(1024)
    print("接收到客户端发来的消息：", data.decode("utf-8"))
    server.sendto("您好,这里是服务端".encode("utf-8"), client)
