# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 15:35:52 2016

@author: Administrator
"""
import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = DmozItem()
            item['title'] = sel.xpath('./a/div[contains(@class,"site-title")]/text()').extract()
            item['link'] = sel.xpath('./a/@href').extract()
            item['desc'] = sel.xpath('./div[@class="site-descr "]').extract()
            yield item