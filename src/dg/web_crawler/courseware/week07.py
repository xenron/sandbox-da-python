# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 10:37:24 2016

@author: lenovo-pc
"""

#####新浪微博API的使用#####
from weibo import APIClient  
import webbrowser#python内置的包 

APP_KEY = '3828324047'  
APP_SECRET = '1f92da9d7a4199ebe8d653aa62fc2ac7'  
CALLBACK_URL = 'http://f.dataguru.cn/'  
  
#利用官方微博SDK  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
#得到授权页面的url，利用webbrowser打开这个url  
url = client.get_authorize_url()  
print url  
webbrowser.open_new(url)  
#http://f.dataguru.cn/?code=367c834cfdfd93e7a77462692edf75ac
#获取code=后面的内容  
code = '367c834cfdfd93e7a77462692edf75ac'

#获取token
r = client.request_access_token(code)  
access_token = r.access_token # 新浪返回的token，类似abc123xyz456  
expires_in = r.expires_in  # token过期的UNIX时间

# 设置得到的access_token  
client.set_access_token(access_token, expires_in)  
  
#获取公共微博更新信息 
#print client.statuses__public_timeline()  
statuses = client.statuses.public_timeline.get(count=10)['statuses']  
length = len(statuses)  
#输出了部分信息  
for i in range(0,length):  
    print u'昵称：'+statuses[i]['user']['screen_name']  
    print u'简介：'+statuses[i]['user']['description']  
    print u'位置：'+statuses[i]['user']['location']  
    print u'微博：'+statuses[i]['text']  

#获取@信息
mentions=client.statuses.mentions.get()['statuses']
len(mentions)
print mentions[0]['created_at']

#####第三方API的使用#####
from urllib import urlencode
import urllib
import json

#配置您申请的APPKey
appkey = "d0a0bc69d60066a9733ef6e24691df3c"
 
#根据城市查询天气
def request1(appkey, m="GET",city="广州",dtype="json"):
    url = "http://op.juhe.cn/onebox/weather/query"
    params = {
        "cityname" : city, #要查询的城市，如：温州、上海、北京
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : dtype, #返回数据的格式,xml或json，默认json
 
    }
    params = urlencode(params,)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            return res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"
        
weather=request1(appkey,"GET")
print weather
print urllib.unquote(weather.get("data").get("realtime").get("wind").get("direct"))

####JSON数据的解析#####
import json
from urllib import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_name")

print(getCountry("50.78.253.58"))

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))


#####google编辑者地理信息#####
from urllib import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import datetime
import json
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    #Format of revision history pages is: 
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "lxml")
    #finds only the links with class "mw-anonuserlink" which has IP addresses 
    #instead of usernames
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")
    
links = getLinks("/wiki/Python_(programming_language)")


while(len(links) > 0):
    for link in links:
        print("-------------------") 
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)

