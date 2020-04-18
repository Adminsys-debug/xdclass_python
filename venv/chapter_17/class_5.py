#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 22:41
# @Author  : mr.chen
# @File    : class_5
# @Software: PyCharm
# @Email   : 794281961@qq.com
#
# import socket, ssl
#
# client = ssl.wrap_socket(socket.socket())
# client.connect(("api.xdclass.net", 443))
# client.send(
#     b'GET /pub/api/v1/web/all_category\r\nHTTP/1.1\r\nHost: api.xdclass.net\r\nConnection: keep-alive\r\nAccept: application/json, text/plain, */*\r\nSec-Fetch-Dest: empty\r\nUser-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\r\nOrigin: https://m.xdclass.net\r\nSec-Fetch-Site: same-site\r\nSec-Fetch-Mode: cors\r\nReferer: https://m.xdclass.net/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9')
#
# # 缓存区
# buffer = []
# while True:
#     recv = client.recv(1024)
#     if recv:
#         buffer.append(recv)
#     else:
#         break
# result = b"".join(buffer)
# client.close()
# print(result.decode("utf-8"))
#
import requests

res = requests.get("https://api.xdclass.net/pub/api/v1/web/all_category")
print(res.content.decode("utf-8"))
