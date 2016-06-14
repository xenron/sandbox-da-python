# -*- coding: utf-8 -*-
import scrapy
from topgoods.items import TopgoodsItem

from collections import OrderedDict
import urllib
import time
import json
import re 

class TmGoodsSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
    )
    #记录处理的页数
    count=0 
    

    def randomtime(self):
        str1=str(time.time()).replace(".",'')
        str2=time.strftime("%H%M", time.localtime())
        return "_".join([str1,str2])
    
    def generate_request(self,response):
        '''获得推荐商品的URL'''
        
        para_dict = OrderedDict()

        text = response.xpath('//textarea[@class="ks-datalazyload"]/script')
        j_command = response.xpath('//div[@id="J_Recommend"]')
        attr = j_command.xpath('@data-p4p-cfg').extract()[0]
        attr_dict = eval(attr)
        para_dict['pid'] = attr_dict['pid']
        
        son_dict = OrderedDict()
        son_dict['sbid'] = 2
        son_dict['frcatid'] = attr_dict['frontcatid']
        son_dict['keyword'] = attr_dict['keyword']
        son_dict['pid'] = attr_dict['pid']
        son_dict['offset'] = 45
        son_dict['propertyid'] = attr_dict['propertyid']
        son_dict['gprice'] = attr_dict['gprice']
        son_dict['loc'] = attr_dict['loc']
        son_dict['sort'] = attr_dict['sort']
        son_dict['feature_names'] = ("promoPrice,multiImgs,tags,dsrDeliver,dsrDeliverGap"
            ",dsrDescribe,dsrDescribeGap,dsrService,dsrServiceGap")
        son_query = urllib.quote(urllib.urlencode(son_dict))
        
        para_dict['qs1'] = son_query
        para_dict['_ksTS'] = self.randomtime()
        para_dict['cb'] = "json519"
        
        end_url = "?".join(["https://mbox.re.taobao.com/gt",urllib.urlencode(para_dict)])
        
        return end_url
        
    def parse_recommand(self,response):
 
        aim_str = re.findall(r'json519\((.*?)\)',response.body)
        
        if aim_str:
            json_obj = json.loads(aim_str[0])
            for obj in json_obj['data']['ds1']:
                item = TopgoodsItem()
                item["GOODS_URL"] = obj['eurl']
                item["GOODS_PRICE"] = obj['price']
                item["GOODS_NAME"] = obj['title']

                yield item 

    def parse(self, response):
    
        TmGoodsSpider.count += 1
        
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        if not divs:
            self.log( "List Page error--%s"%response.url )

        rec_url = self.generate_request(response)
        
        yield scrapy.Request(url=rec_url,callback=self.parse_recommand,dont_filter=True,
            )
        
        for div in divs:
            item=TopgoodsItem()
            #商品价格
            item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            #商品名称
            item["GOODS_NAME"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            #商品连接
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["GOODS_URL"] = pre_goods_url if "http:" in pre_goods_url else ("http:"+pre_goods_url)
            
            yield scrapy.Request(url=item["GOODS_URL"],meta={'item':item},callback=self.parse_detail,
                dont_filter=True)
        

    def parse_detail(self,response):

        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log( "Detail Page error--%s"%response.url )
            
        item = response.meta['item']
        div=div[0]
        #店铺名称
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        #店铺连接
        item["SHOP_URL"] = response.urljoin(div.xpath("li[1]/div/a/@href")[0].extract())
        #公司名称
        item["COMPANY_NAME"] = div.xpath("li[3]/div/text()")[0].extract().strip()
        #公司所在地
        item["COMPANY_ADDRESS"] = div.xpath("li[4]/div/text()")[0].extract().strip()
        
        yield item