#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:22
# @Author  : mr.chen
# @File    : url_manager
# @Software: PyCharm
# @Email   : 794281961@qq.com


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def get_new_url(self):
        """
        获取新的url
        :return:
        """
        return self.new_urls.pop()

    def add_new_url(self, url):
        """
        添加新的url
        :param url: 新的url
        :return:
        """
        self.new_urls.add(url)

    def add_old_url(self, url):
        """
        添加已经爬取过的url
        :param url: 已经爬取过的url
        :return:
        """
        self.old_urls.add(url)
