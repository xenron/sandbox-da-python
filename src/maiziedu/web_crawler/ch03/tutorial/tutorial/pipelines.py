# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb

DBKWARGS={'db':'test','user':'root', 'passwd':'',
    'host':'localhost','use_unicode':True, 'charset':'utf8'}

class TutorialPipeline(object):

    def __init__(self):
        try:
            self.con = MySQLdb.connect(**DBKWARGS)
        except Exception,e:
            print "Connect db error:",e
        
    def process_item(self, item, spider):
        cur = self.con.cursor()
        sql = "insert into dmoz_book values(%s,%s,%s)"
        lis = (''.join(item["title"]),''.join(item["link"]),
            ''.join(item["desc"]))
        try:
            cur.execute(sql,lis)
        except Exception,e:
            print "Insert error:",e
            self.con.rollback()
        else:
            self.con.commit()
        cur.close()
        return item

    def __del__(self):
        try:
            self.con.close()
        except Exception,e:
            print "Close db error",e