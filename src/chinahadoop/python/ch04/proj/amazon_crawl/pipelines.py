# -*- coding: utf-8 -*-
from scrapy.exporters import JsonItemExporter, CsvItemExporter, XmlItemExporter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BestsellerItemJsonPipeline(object):
    
    def open_spider(self, spider):
        self.file = open('amazon_bestseller.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
         
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
     
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    
class BestsellerItemCsvPipeline(object):
    
    def open_spider(self, spider):
        self.file = open('amazon_bestseller.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
         
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
     
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    
class BestsellerItemXmlPipeline(object):
    
    def open_spider(self, spider):
        self.file = open('amazon_bestseller.xml', 'wb')
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()
         
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
     
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
