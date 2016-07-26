# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:08:24 2016

@author: Administrator
"""
import urllib2

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
            
        response = urllib2.urlopen(url)
        
        if response.getcode()!=200:
            return None
        
        return response.read()
        
        