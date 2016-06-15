# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaiziItem(scrapy.Item):
    # define the fields for your item here like:
    LessID = scrapy.Field()
    LessName = scrapy.Field()
    LessHref = scrapy.Field()
    LessVideo = scrapy.Field()
    pLessID = scrapy.Field()
    pLessName = scrapy.Field()
    pLessHref = scrapy.Field()
    pass
