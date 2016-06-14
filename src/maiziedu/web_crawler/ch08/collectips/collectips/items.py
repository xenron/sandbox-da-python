# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectipsItem(scrapy.Item):
    # define the fields for your item here like:
    IP = scrapy.Field() #代理ip
    PORT = scrapy.Field() #端口
    TYPE = scrapy.Field() #代理类型
    POSITION = scrapy.Field() #代理的位置
    SPEED = scrapy.Field() #速度
    LAST_CHECK_TIME = scrapy.Field() #最后验证时间
    
