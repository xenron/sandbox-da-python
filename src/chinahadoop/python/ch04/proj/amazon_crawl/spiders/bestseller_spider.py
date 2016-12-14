# -*- coding: utf-8 -*-

'''
Created on Dec 2, 2016

@author: Bin Liang
'''

import scrapy
from amazon_crawl.items import BestsellerItem

class BestsellerSinglePageSpider(scrapy.Spider):
    name = "bestseller_single_page"
    
    allowed_domains = ['amazon.cn']
    
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1',
    ]
    
    def parse(self, response):
        div_zg_itemRow_lst = response.xpath('//div[@class="zg_itemRow"]')
        
        for div_zg_itemRow in div_zg_itemRow_lst:
            item = BestsellerItem()
            item['rank_number'] = div_zg_itemRow.xpath('.//span[@class="zg_rankNumber"]/text()').extract_first()
            item['book_name'] = div_zg_itemRow.xpath('.//a[@class="a-link-normal"]/text()')[2].extract()
            item['author'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-base"]/text()').extract_first()
            item['star_rank'] = div_zg_itemRow.xpath('.///span[@class="a-icon-alt"]/text()').extract_first()
            item['book_type'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-secondary"]/text()').extract_first()
            item['price'] = div_zg_itemRow.xpath('.//span[@class="a-size-base a-color-price"]/text()').extract_first()
            
            yield item
            

class BestsellerMultiPageSpider(scrapy.Spider):
    name = "bestseller_multi_page"
    
    allowed_domains = ['amazon.cn']
    
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1',
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_3?ie=UTF8&pg=2',
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_5?ie=UTF8&pg=3',
    ]
    
    def parse(self, response):
        div_zg_itemRow_lst = response.xpath('//div[@class="zg_itemRow"]')
        
        for div_zg_itemRow in div_zg_itemRow_lst:
            item = BestsellerItem();
            item['rank_number'] = div_zg_itemRow.xpath('.//span[@class="zg_rankNumber"]/text()').extract_first()
            item['book_name'] = div_zg_itemRow.xpath('.//a[@class="a-link-normal"]/text()')[2].extract()
            item['author'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-base"]/text()').extract_first()
            item['star_rank'] = div_zg_itemRow.xpath('///span[@class="a-icon-alt"]/text()').extract_first()
            item['book_type'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-secondary"]/text()').extract_first()
            item['price'] = div_zg_itemRow.xpath('.//span[@class="a-size-base a-color-price"]/text()').extract_first()
            
            yield item
            
            
class BestsellerAutoPageSpider(scrapy.Spider):
    name = "bestseller_auto_page"
    
    allowed_domains = ['amazon.cn']
    
    start_urls = [
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1',
    ]
    
    def parse(self, response):
        div_zg_itemRow_lst = response.xpath('//div[@class="zg_itemRow"]')
        
        for div_zg_itemRow in div_zg_itemRow_lst:
            item = BestsellerItem();
            item['rank_number'] = div_zg_itemRow.xpath('.//span[@class="zg_rankNumber"]/text()').extract_first()
            item['book_name'] = div_zg_itemRow.xpath('.//a[@class="a-link-normal"]/text()')[2].extract()
            item['author'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-base"]/text()').extract_first()
            item['star_rank'] = div_zg_itemRow.xpath('///span[@class="a-icon-alt"]/text()').extract_first()
            item['book_type'] = div_zg_itemRow.xpath('.//span[@class="a-size-small a-color-secondary"]/text()').extract_first()
            item['price'] = div_zg_itemRow.xpath('.//span[@class="a-size-base a-color-price"]/text()').extract_first()
            
            yield item
            
        xpath_next_page = './/li[@class="zg_page zg_selected"]/following-sibling::li/a/@href'
        if response.xpath(xpath_next_page):
            url_next_page = response.xpath(xpath_next_page).extract_first()
            request = scrapy.Request(url_next_page, callback = self.parse)
            yield request
        