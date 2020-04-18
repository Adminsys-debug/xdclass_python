#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:20
# @Author  : mr.chen
# @File    : html_parser
# @Software: PyCharm
# @Email   : 794281961@qq.com
import re
from html_downloader import HtmlDownloader
from product import Product


# html解析器


class HtmlParser:
    item_pattern = r'<li class="brick-item">[\s\S]*?</li>'
    # 通过re的组可以获取标签里面的文本
    title_pattern = r'<h3 class="title"><a href="javascript:;">([\s\S]*?)</a></h3>'
    desc_pattern = r'<p class="desc">([\s\S]*?)</p>'
    price_pattern = r'<span class="num">([\s\S]*?)</span>'

    def parser(self, html):
        """
        解析给定的html
        :param html:html
        :return: product set
        """
        items_ = re.findall(self.item_pattern, html)
        res = set()
        for i in items_:
            title = re.findall(self.title_pattern, i)
            desc = re.findall(self.desc_pattern, i)
            price = re.findall(self.price_pattern, i)
            res.add(Product(title[0], desc[0], price[0]))

        return res

# downloader = HtmlDownloader()
# html = downloader.download("http://127.0.0.1:8848/xiaomi-master/index.html")
# htmlParser = HtmlParser()
# res = htmlParser.parser(html)
# for i in res:
#     print(i)
