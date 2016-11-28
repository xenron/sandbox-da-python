# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 10:51:56 2016

@author: Administrator
"""

from urllib import urlopen;  #载入urllib.request,用于获取页面html源代码
from pandas import Series;  #载入series包
from pandas import DataFrame;   #载入dataframe包
from bs4 import BeautifulSoup;  #载入beautifulsoup包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##初始化数据
#评分
score=[]
#商品名称
goods_name=[]
#评论时间
times=[]
#文字评论
comments=[]
#会员名称
user_id=[]
#会员等级
user_grade=[]
#地区
area=[]
#客户端
com_client=[]

#抓取页面
driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://item.jd.com/636920.html#comment")
time.sleep(5)

#好评
driver.find_element_by_xpath('//*[@id="comments-list"]/div[1]/div/ul/li[3]/a').click()    
time.sleep(5)


#抓取评论数据
def get_comment(num=2):
    num=str(num)
    while len(score)<1000:
        datas=driver.find_element_by_id("comment-"+num).find_elements_by_class_name("comments-item")
        for data in datas:
            try:
                tmps=data.find_elements_by_class_name('column')
            except:
                continue
            tmp1=tmps[0].find_elements_by_tag_name('div')
            try:
                score.append(tmp1[0].get_attribute('class'))
            except:
                score.append('')
            try:
                times.append(tmps[0].find_element_by_class_name('comment-time').text)
            except:
                times.append('')
            try:
                goods_name.append(tmp1[3].text)
            except:
                goods_name.append('')
            try:
                comments.append(tmps[1].find_element_by_class_name('p-comment').text)
            except:
                comments.append('')
            tmp3=tmps[2].find_elements_by_tag_name('div')
            try:
                user_id.append(tmp3[0].text)
            except:
                user_id.append('')
            try:
                user_grade.append(tmp3[2].find_element_by_class_name('u-vip-level').text)
            except:
                user_grade.append('')
            try:
                area.append(tmp3[2].find_element_by_class_name('u-addr').text)
            except:
                area.append('')
            try:
                com_client.append(tmp3[3].text)
            except:
                com_client.append('')
        driver.find_element_by_id("comment-"+num).find_element_by_class_name('ui-pager-next').click()
        time.sleep(1)
        

#差评
driver.find_element_by_xpath('//*[@id="comments-list"]/div[1]/div/ul/li[5]/a').click()    
time.sleep(5)

get_comment()   

#保存数据
result=DataFrame({'times':times,'user_id':user_id,'user_grade':user_grade,'area':area,'goods_name':goods_name,
                    'score':score,'com_client':com_client,'comment':comments})

result.to_csv('d:/result2.csv',encoding='utf-8')