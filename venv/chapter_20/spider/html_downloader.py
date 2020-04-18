#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:19
# @Author  : mr.chen
# @File    : html_downloader
# @Software: PyCharm
# @Email   : 794281961@qq.com
import requests


# html下载器
class HtmlDownloader:

    def download(self, url):
        """
        根据给定的url下载网页
        :param url:url
        :return: 下载好的文本
        """
        res = requests.get(url)
        return res.content.decode("utf-8")
