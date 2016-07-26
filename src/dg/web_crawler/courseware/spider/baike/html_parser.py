# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:08:39 2016

@author: Administrator
"""
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self,page_url,soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
#        summary_node = soup.find('div',class_='lemma-summary')
#        res_data['summary'] = summary_node.get_text()
        
        #<div class="para" label-module="para">天空<a target="_blank" href="/view/37.htm">
        content_node = soup.findAll('div',class_='para')
        n=len(content_node)
        content={}
        for i in range(n):
            content[i]= content_node[i].get_text()
        res_data['content'] = content
        
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
            
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data