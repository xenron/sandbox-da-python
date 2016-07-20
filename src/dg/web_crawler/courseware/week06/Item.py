# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 10:44:09 2016

@author: Administrator
"""

#声明Item
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
product['price']

product['last_updated']

product.get('last_updated', 'not set')

product['lala'] 
 
product.get('lala', 'unknown field')

'name' in product

'last_updated' in product

'last_updated' in product.fields

'lala' in product.fields

#设置字段的值
product['last_updated'] = 'today'
product['last_updated']

product['lala'] = 'test'

#获取所有值
product.keys()
product.items()

#复制Item
product2 = Product(product)
print product2

product3 = product2.copy()
print product3

#根据Item创建字典
dict(product)

#根据字典创建Item
Product({'name':'Laptop PC','price':1500})

#扩展Item
class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()
    

    


