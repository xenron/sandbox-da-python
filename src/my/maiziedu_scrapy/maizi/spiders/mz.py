__author__ = 'Administrator'

from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
import sys, json, re
from maizi.items import MaiziItem

reload(sys)
sys.setdefaultencoding("utf-8")


class qtscrapy(BaseSpider):
    name = "mz"
    base_url = "http://api2.qingting.fm/v6/media/recommends/guides/section/"
    start_urls = ["http://www.maiziedu.com/course/web/", ]
    allowed_domains = ["www.maiziedu.com"]

    def parse(self, response):
        playlist = Selector(text=response.body).css('div.lead-img a').extract()
        for p in playlist:
            meta = {}
            pLessHref = 'http://www.maiziedu.com/' + Selector(text=p).xpath("//a/@href").extract()[0]
            pLessID = str(pLessHref)[str(pLessHref).rindex('/') + 1:]
            pLessName = Selector(text=p).xpath("//a/@title").extract()[0]
            meta["pLessID"] = pLessID
            meta["pLessHref"] = pLessHref
            meta["pLessName"] = pLessName
            yield Request(url=pLessHref, callback=self.parse_course, meta={"meta": meta})

    def parse_course(self, response):
        playlist = Selector(text=response.body).xpath('//*[@id="playlist"]/ul/li/a').extract()
        for p in playlist:
            meta = {}
            LeesionID = Selector(text=p).xpath('//a/@lesson_id').extract()[0]
            href = "http://www.maiziedu.com/course" + Selector(text=p).xpath('//a/@href').extract()[0]
            Leesion = Selector(text=p).xpath('//a/text()').extract()[0]
            meta["LessID"] = LeesionID
            meta["LessHref"] = href
            meta["LessName"] = Leesion
            meta["pLessID"] =  response.meta["meta"]["pLessID"]
            meta["pLessHref"] = response.meta["meta"]["pLessHref"]
            meta["pLessName"] = response.meta["meta"]["pLessName"]
            yield Request(href, callback=self.get_course_video, meta={"meta": meta})

    def get_course_video(self, response):
        # print(response)
        mzitem = MaiziItem();
        mzitem = response.meta['meta']
        re_video = re.search(r'<source src="(.*?).mp4"', response.body, re.S)
        if re_video is not None:
            video = re_video.group(1) + ".mp4"
            mzitem["LessVideo"] = video
            yield mzitem
