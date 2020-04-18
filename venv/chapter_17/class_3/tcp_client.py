#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 10:35
# @Author  : mr.chen
# @File    : tcp_client
# @Software: PyCharm
# @Email   : 794281961@qq.com
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8888))
print("客户端已经启动,已完成连接")

# 客户端接受的数据大小
# server_data = client.recv(1024)
# print("请输入要发送的内容: ")
# client.send(input().encode("utf-8"))
# print("接收到服务端的响应: ", server_data.decode("utf-8"))
# if server_data.decode("utf-8") != "serverCloser":
#     print("请输入要发送的内容: ")
#     client.send(input().encode("utf-8"))
#     print("接收到服务端的响应: ", server_data.decode("utf-8"))
# elif server_data.decode("utf-8") == "serverCloser":
#     client.close()
while True:
    print("请输入要发送的内容: ")
    # 获取输入,判断是否是close
    data = input()
    client.send(data.encode("utf-8"))
    if data == "close":
        client.close()
        print("客户端关闭连接")
        break
    recv_data = client.recv(1024).decode("utf-8")
    print("接收到服务器的响应：", recv_data)
