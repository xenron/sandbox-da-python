# -*- coding: utf-8 -*-

# Scrapy settings for collectips project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'collectips'

SPIDER_MODULES = ['collectips.spiders']
NEWSPIDER_MODULE = 'collectips.spiders'

# database connection parameters
DBKWARGS={'db':'ippool','user':'root', 'passwd':'toor',
    'host':'localhost','use_unicode':True, 'charset':'utf8'}


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'collectips.pipelines.CollectipsPipeline': 300,
}

#Configure log file name
LOG_FILE = "scrapy.log"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'

