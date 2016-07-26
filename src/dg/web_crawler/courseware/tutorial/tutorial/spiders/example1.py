# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 15:48:44 2016

@author: Administrator
"""

import scrapy

class MySpider(scrapy.Spider):
    name = 'example1'
    allowed_domains = ['dataguru.cn']
    start_urls = [
        'http://www.dataguru.cn',
        'http://bi.dataguru.cn/article-9581-1.html',
        'http://vc.dataguru.cn/article-9576-1.html'
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)