# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:07:51 2016

@author: Administrator
"""
import url_manager,html_downloader,html_parser,html_outputer
reload(html_outputer)
reload(html_parser)

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
        
    def craw(self,root_rul):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d:%s' %(count,new_url)
            except:
                print 1
            try:               
                html_cont=self.downloader.download(new_url)
            except: 
                print 2
            try: 
                new_urls,new_data=self.parser.parse(new_url,html_cont)
            except:
                print 3
            try:
                self.urls.add_new_urls(new_urls)
            except:
                print 4
            try:
                self.outputer.collect_data(new_data)
            except:
                print 5
            
                
            count=count+1
            if count == 10000:
                break
#            except:
#                print 'craw failed'
        try:    
            self.outputer.output_html()
        except:
            print 6
            


if __name__=="__main__":
    root_url='http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    