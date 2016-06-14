# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bioon.handledb import adb_insert_data,exec_sql
from bioon.settings import DBAPI,DBKWARGS

class BioonPipeline(object):
    def process_item(self, item, spider):
        print "Now in pipeline:"
        print item['name']
        print item['value']
        print "End of pipeline."
        #store data
        #adb_insert_data(item,"tablename",DBAPI,**DBKWARGS)
        return item
