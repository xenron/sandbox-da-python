# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BestsellerItem(scrapy.Item):
    # define the fields for your item here like:
    rank_number = scrapy.Field()    # 排名
    book_name = scrapy.Field()      # 书名
    author = scrapy.Field()         # 作者
    star_rank = scrapy.Field()      # 星级评分
    book_type = scrapy.Field()      # 装订类别
    price = scrapy.Field()          # 价格
    
