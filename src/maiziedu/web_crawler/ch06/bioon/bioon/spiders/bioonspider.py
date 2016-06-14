# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import FormRequest

from bioon import settings
from bioon.items import BioonItem

class BioonspiderSpider(scrapy.Spider):
    name = "bioonspider"
    allowed_domains = ["bioon.com"]
    start_urls=['http://login.bioon.com/login']
    
    def parse(self,response):
        
        #从response.headers中获取cookies信息
        r_headers = response.headers['Set-Cookie']
        cookies_v = r_headers.split(';')[0].split('=')
        
        cookies = {cookies_v[0]:cookies_v[1]}
        
        #模拟请求的头部信息
        headers = {
        'Host':	'login.bioon.com',
        'Referer':'http://login.bioon.com/login',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        'X-Requested-With':'XMLHttpRequest' 
        }
        
        #获取验证信息
        csrf_token = response.xpath(
            '//input[@id="csrf_token"]/@value').extract()[0]
        
        #获得post的目的URL
        login_url = response.xpath(
            '//form[@id="login_form"]/@action').extract()[0]
        end_login = response.urljoin(login_url)
        
        #生成post的数据
        formdata={
        #请使用自己注册的用户名
        'account':'********',
        'client_id':'usercenter',
        'csrf_token':csrf_token,
        'grant_type':'grant_type',
        'redirect_uri':'http://login.bioon.com/userinfo',
        #请使用自己注册的用户名
        'username':'********',
        #请使用自己用户名的密码
        'password':'xxxxxxx',
        }
        
        #模拟登录请求
        return FormRequest(
        end_login,
        formdata=formdata,
        headers=headers,
        cookies=cookies,
        callback=self.after_login
        )

    def after_login(self,response):
        
        self.log('Now handling bioon login page.')
        
        aim_url = 'http://news.bioon.com/Cfda/'
        
        obj = json.loads(response.body)
        
        print "Loging state: ", obj['message']
        if "success" in obj['message']:
            self.logger.info("=========Login success.==========")
        
        return scrapy.Request(aim_url,callback = self.parse_list)
    
    def parse_list(self,response):
        
        lis_news = response.xpath(
            '//ul[@id="cms_list"]/li/div/h4/a/@href').extract()
        
        for li in lis_news:
            end_url = response.urljoin(li)
            yield scrapy.Request(end_url,callback=self.parse_content)
    
    def parse_content(self,response):
        
        head = response.xpath(
            '//div[@class="list_left"]/div[@class="title5"]')[0]
        
        item=BioonItem()
        
        item['title'] = head.xpath('h1/text()').extract()[0]
            
        item['source'] = head.xpath('p/text()').re(ur'来源：(.*?)\s(.*?)$')[0]
        
        item['date_time'] = head.xpath('p/text()').re(ur'来源：(.*?)\s(.*?)$')[1]
        
        item['body'] = response.xpath(
            '//div[@class="list_left"]/div[@class="text3"]').extract()[0]
        
        return item