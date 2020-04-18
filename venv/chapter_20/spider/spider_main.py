#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:21
# @Author  : mr.chen
# @File    : spider_main
# @Software: PyCharm
# @Email   : 794281961@qq.com

from data_storage import DataStorage
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from product import Product
from url_manager import UrlManager


class SpiderMain:
    def __init__(self):
        self.url_manager = UrlManager()
        self.html_downloader = HtmlDownloader()
        self.html_parser = HtmlParser()
        self.data_storage = DataStorage()

    def start(self):
        """
        爬虫的主启动方法
        :return:
        """
        self.url_manager.add_new_url("http://127.0.0.1:8848/xiaomi-master/index.html")
        # 从url管理器获取url
        url = self.url_manager.get_new_url()
        # 将获取到的url使用下载器进行下载
        html = self.html_downloader.download(url)
        # 将html进行解析
        res = self.html_parser.parser(html)
        # 数据存储
        self.data_storage.storage(res)


if __name__ == '__main__':
    main = SpiderMain()
    main.start()
