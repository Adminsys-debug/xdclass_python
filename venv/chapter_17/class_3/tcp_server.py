#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 10:33
# @Author  : mr.chen
# @File    : tcp_server
# @Software: PyCharm
# @Email   : 794281961@qq.com
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8888))
# 允许最多5个客户端连接
server.listen(5)
print("服务端已经启动, 等待客户端连接========>>")
client, address = server.accept()
print("已经建立连接")
# 接受的数据大小
# data = client.recv(1024)
# print("服务端接收到的数据：", data.decode("utf-8"))
# while data.decode("utf-8") != "close":
#     print("请输入回复的内容: ")
#     client.send(input().encode("utf-8"))
#     if data.decode("utf-8") == "close":
#         client.send("serverCloser".encode("utf-8"))
#         server.close()
while True:
    # 接受客户端发送的数据
    data = client.recv(1024).decode("utf-8")
    # 判断数据是否是close
    if data == "close":
        # 如果是close,那关闭server,并且退出循环
        print("服务端关闭连接")
        server.close()
        break
        # 如果不是,那打印接收到的数据,并且给客户端响应
    print("客户端发送的内容：", data)
    print("请输入给客户端回复的内容")
    client.send(input().encode("utf-8"))
