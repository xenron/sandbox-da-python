# -*- coding: utf-8 -*-

# Scrapy settings for bioon project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#
#Scrapy项目实现的bot的名字(也为项目名称)。
BOT_NAME = 'bioon'

SPIDER_MODULES = ['bioon.spiders']
NEWSPIDER_MODULE = 'bioon.spiders'

#保存项目中启用的下载中间件及其顺序的字典。默认:: {}
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'

#保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 
#不过值(value)习惯设定在0-1000范围内。
ITEM_PIPELINES={
#'bioon.pipelines.BioonPipeline':500
}

#下载器下载网站页面时需要等待的时间。该选项可以用来限制爬取速度， 
#减轻服务器压力。同时也支持小数:
DOWNLOAD_DELAY = 0.25    # 250 ms of delay

#爬取网站最大允许的深度(depth)值。如果为0，则没有限制。
DEPTH_LIMIT=0

#是否启用DNS内存缓存(DNS in-memory cache)。默认: True
DNSCACHE_ENABLED=True

#logging输出的文件名。如果为None，则使用标准错误输出(standard error)。默认: None
LOG_FILE='scrapy.log'

#log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG。默认: 'DEBUG'
LOG_LEVEL='DEBUG'

#如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。
#例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
#默认: False
LOG_STDOUT=False

#对单个网站进行并发请求的最大值。默认: 8
CONCURRENT_REQUESTS_PER_DOMAIN=8

#Default: True ,Whether to enable the cookies middleware. If disabled, no cookies will be sent to web servers.
COOKIES_ENABLED = True

#feed settings
FEED_URI = 'file:///C:/Users/stwan/Desktop/bioon/a.txt'
FEED_FORMAT = 'jsonlines'

LOG_ENCODING = None

##----------------------Mail settings------------------------
#Default: ’scrapy@localhost’,Sender email to use (From: header) for sending emails.
MAIL_FROM='*********@163.com'

#Default: ’localhost’, SMTP host to use for sending emails.
MAIL_HOST="smtp.163.com"

#Default: 25, SMTP port to use for sending emails.
MAIL_PORT="25"

#Default: None, User to use for SMTP authentication. If disabled no SMTP authentication will be performed.
MAIL_USER="*********@163.com"

#Default: None, Password to use for SMTP authentication, along with MAIL_USER.
MAIL_PASS="xxxxxxxxxxxxx"

#Enforce using STARTTLS. STARTTLS is a way to take an existing insecure connection, 
#and upgrade it to a secure connection using SSL/TLS.
MAIL_TLS=False

#Default: False, Enforce connecting using an SSL encrypted connection
MAIL_SSL=False