import scrapy

class ZaobaoSpider(scrapy.Spider):
	name = "zaobao"
	start_urls=["http://www.zaobao.com/special/report/politic/fincrisis"]

	def parse(self, response):
		for href in response.css('#l_title .l_title a::attr(href)'):
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback=self.parse_news)

	def parse_news(self, response):
		yield {
			'title':response.css('#a_title h1::text').extract()[0],
			'dt':response.css("#a_credit .time::text").extract()[0],
			'body':response.css("#article_content").extract()[0],
			'link': response.url,
		}