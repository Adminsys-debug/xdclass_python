#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 10:05
# @Author  : mr.chen
# @File    : udp_client
# @Software: PyCharm
# @Email   : 794281961@qq.com
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("您好,我是客户端".encode("utf-8"), ("127.0.0.1", 8888))
data, server = client.recvfrom(1024)
print(data.decode("utf-8"))
client.close()