# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 22:25:23 2016

@author: lenovo-pc
"""

#启动终端
scrapy shell 'http://scrapy.org' --nolog

#使用终端
sel.xpath("//h2/text()").extract()[0]
fetch("http://slashdot.org")
sel.xpath('//title/text()').extract()
request = request.replace(method="POST")
fetch(request)

import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

response.url
sel.xpath('//h1[@class="fn"]')
view(response)
^D