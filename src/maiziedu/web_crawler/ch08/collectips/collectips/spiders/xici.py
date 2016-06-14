# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from collectips.items import CollectipsItem


class proxySpider(CrawlSpider):
    
    name="xici"
    allowed_domains=["xici.net.co",]
    start_urls=[
        'http://www.xici.net.co/nn/1',
        'http://www.xici.net.co/nn/2',
        'http://www.xici.net.co/nn/3',
        'http://www.xici.net.co/nn/4',
        'http://www.xici.net.co/nn/5',
        ]
    def parse(self,response):
        ip_list=response.xpath('//table[@id="ip_list"]')
        ips=ip_list[0].xpath('tr')
        items=[]
        for ip in ips[1:]:
            pre_item=CollectipsItem()
            tds=ip.xpath('td')

            ip_address=tds[2].xpath('text()')[0].extract()
            pre_item["IP"] = ip_address
            
            port=tds[3].xpath('text()')[0].extract()
            pre_item["PORT"] = port
            
            location=tds[4].xpath('string(.)')[0].extract().strip()
            pre_item["POSITION"] = location
            
            proxy_type=tds[6].xpath('text()')[0].extract()
            pre_item["TYPE"] = proxy_type
            
            speed=tds[8].xpath('div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            pre_item["SPEED"] = speed

            check_time=tds[9].xpath('text()')[0].extract()
            pre_item["LAST_CHECK_TIME"] = check_time

            items.append(pre_item)
        return items
