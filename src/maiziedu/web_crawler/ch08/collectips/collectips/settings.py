# -*- coding: utf-8 -*-

# Scrapy settings for collectips project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'collectips'

SPIDER_MODULES = ['collectips.spiders']
NEWSPIDER_MODULE = 'collectips.spiders'

ITEM_PIPELINES={
    "collectips.pipelines.CollectipsPipeline":400,
}

LOG_FILE = "scrapy.log"

DBAPI = "MySQLdb"
DBKWARGS = {
    'db':'test','user':'root', 'passwd':'',
    'host':'localhost', 'charset':'utf8',
}
AIM_TABLE = "proxy"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'

RETRY_ENABLED = True
RETRY_TIMES = 5  
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 801, 404, 403,302,303,301,307]

#my extension
EXTENSIONS ={
    'collectips.extension.MyExtension.SpiderOpenCloseLogging':500,
    'collectips.extension.MyExtension.MyStatsExtension':501,
}

MYEXT_ENABLED = True
MYEXT_ITEMCOUNT = 10

#memory usage
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 0
MEMUSAGE_REPORT = True