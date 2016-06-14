# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from collectips.handledb import adb_insert_data
from collectips.settings import AIM_TABLE
import logging

class CollectipsPipeline(object):
    def __init__(self,crawler):
        self.table = crawler.settings.get('AIM_TABLE')

    def process_item(self, item, spider):
        spider.logger.info("There is a item will be stored.")
        adb_insert_data(item,self.table)
        return item
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)