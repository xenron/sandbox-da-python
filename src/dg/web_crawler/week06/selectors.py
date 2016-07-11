# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 15:21:17 2016

@author: Administrator
"""

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '<html><body><span>good</span></body></html>'
Selector(text=body).xpath('//span/text()').extract()

response = HtmlResponse(url='http://example.com', body=body)
Selector(response=response).xpath('//span/text()').extract()

response.selector.xpath('//span/text()').extract()

#打开shell
scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html

response.selector.xpath('//title/text()')

response.xpath('//title/text()')

response.css('title::text')

response.xpath('//title/text()').extract()

response.css('title::text').extract()

response.xpath('//base/@href').extract()

response.css('base::attr(href)').extract()

response.xpath('//a[contains(@href, "image")]/@href').extract()

response.css('a[href*=image]::attr(href)').extract()

response.xpath('//a[contains(@href, "image")]/img/@src').extract()

response.css('a[href*=image] img::attr(src)').extract()

#嵌套选择器
links = response.xpath('//a[contains(@href, "image")]')
links.extract()

for index, link in enumerate(links):
        args = (index, link.xpath('@href').extract(), link.xpath('img/@src').extract())
        print 'Link number %d points to url %s and image %s' % args
        
#结合正则表达式
response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
 
#使用相对XPaths
divs = response.xpath('//div')

for p in divs.xpath('//p'):  # this is wrong - gets all <p> from the whole document
         print p.extract()
         
for p in divs.xpath('.//p'):  # extracts all <p> inside
         print p.extract()
         
for p in divs.xpath('p'):
         print p.extract()
         
#EXSLT扩展
from scrapy import Selector
doc = """
<div>
     <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 """
sel = Selector(text=doc, type="html")
sel.xpath('//li//@href').extract()

sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()

#集合操作
doc = """
<div itemscope itemtype="http://schema.org/Product">
  <span itemprop="name">Kenmore White 17" Microwave</span>
  <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
  <div itemprop="aggregateRating"
    itemscope itemtype="http://schema.org/AggregateRating">
   Rated <span itemprop="ratingValue">3.5</span>/5
   based on <span itemprop="reviewCount">11</span> customer reviews
  </div>

  <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
    <span itemprop="price">$55.00</span>
    <link itemprop="availability" href="http://schema.org/InStock" />In stock
  </div>
  Product description:
  <span itemprop="description">0.7 cubic feet countertop microwave.
  Has six preset cooking categories and convenience features like
  Add-A-Minute and Child Lock.</span>
  Customer reviews:
  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Not a happy camper</span> -
    by <span itemprop="author">Ellie</span>,
    <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1">
      <span itemprop="ratingValue">1</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">The lamp burned out and now I have to replace
    it. </span>
  </div>

  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Value purchase</span> -
    by <span itemprop="author">Lucas</span>,
    <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1"/>
      <span itemprop="ratingValue">4</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">Great microwave for the price. It is small and
    fits in my apartment.</span>
   </div>
 </div>
"""

for scope in Selector(text=doc).xpath('//div[@itemscope]'):
     print "current scope:", scope.xpath('@itemtype').extract()
     props = scope.xpath('''
                 set:difference(./descendant::*/@itemprop,
                                .//*[@itemscope]/*/@itemprop)''')
     print "    properties:", props.extract()
     print

#XPATH小技巧
from scrapy import Selector
sel = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')

sel.xpath('//a//text()').extract() 

sel.xpath("string(//a[1]//text())").extract()    

sel.xpath("//a[1]").extract()    

sel.xpath("string(//a[1])").extract() 

sel.xpath("//a[contains(.//text(), 'Next Page')]").extract()

sel.xpath("//a[contains(., 'Next Page')]").extract()

##
sel = Selector(text="""
    <ul class="list">
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    <ul class="list">
        <li>4</li>
        <li>5</li>
        <li>6</li>
    </ul>""")
xp = lambda x: sel.xpath(x).extract()

xp("//li[1]")

xp("(//li)[1]")

xp("//ul/li[1]")

xp("(//ul/li)[1]")
 
 
sel = Selector(text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>')
sel.css('.shout').xpath('./time/@datetime').extract()

