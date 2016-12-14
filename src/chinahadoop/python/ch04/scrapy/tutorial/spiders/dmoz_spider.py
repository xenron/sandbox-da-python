# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz_spider"
    
    allowed_domains = ['dmoz.org/']
    start_urls = ['http://www.dmoz.org/']

    def parse(self, response):
        aside_nodes = response.xpath('//aside')
        for aside_node in aside_nodes:
            item = DmozItem()
            top_cat = aside_node.xpath('.//h2//a/text()').extract()
            sub_cat = aside_node.xpath('.//h3//a/text()').extract()
            
            item['top_cat'] = top_cat
            item['sub_cat'] = sub_cat
            
            yield item