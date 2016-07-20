# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 10:23:22 2016

@author: Administrator
"""
#Item声明
import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

#创建Item
product = Product(name='Desktop PC', price=1000)
print product

#获取字段的值
product['name']
product.get('name')