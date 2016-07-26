# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:26:40 2016

@author: Administrator
"""

import scrapy
from tieba.items import tiebaitem


class BbsSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8&pn=0",]
    
    def parse(self, response):
            item=tiebaitem()
            title = response.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/text()').extract()
            author = response.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[2]/span[1]/span[2]/a/text()').extract()
            reply = response.xpath('//*[@id="thread_list"]/li/div/div[1]/span/text()').extract()
     
            item['title']=[t.encode('utf-8') for t in title]
            item['author']=[l.encode('utf-8') for l in author]
            item['reply']=[d.encode('utf-8') for d in reply]
            yield item













    
