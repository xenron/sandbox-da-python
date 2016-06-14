#-*- coding:utf-8 -*-
import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']
    
    def start_requests(self):
        url = "http://db.bioon.com/list.php?channelid=1016&classid=951"
        cookies = {
            'dz_username':'wst_today',
            'dz_uid':'1322052',
            'buc_key':'ofR1I78RBaCHkGp8MdBBRjMx7ustawtY',
            'buc_token':'a91b8fef55c66846d3975a9fd8883455'
        }
        return [
            scrapy.Request(url,cookies=cookies),
        ]
    
    def parse(self, response):
        ele = response.xpath(
            '//table[@class="table table-striped"]/thead/tr/th[1]/text()'
            ).extract()
        if ele:
            print "success"
            