# -*- coding: utf-8 -*-
from urllib2 import urlopen #加载urllib2库中的urlopen函数
#通过urlopen函数读取url地址中的全部HTML代码
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
#打印html代码的内容
print(html.read())


#加载BeautifulSoup
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
#通过BeautifulSoup将HTML代码转换为BeautifulSoup对象
bsObj = BeautifulSoup(html.read())
#打印h1标签的内容
print(bsObj.h1)

#加载HTTPError
from urllib2 import HTTPError

##调试程序
#报错
try:
    html=urlopen("http://www.pythonscraping.com/exercise1.html")
except HTTPError as e:
    print(e)
else:
    if html is None:
        print("Url is nor found")

#标签不存在
print(bsObj.nonExistentTag)

print(bsObj.nonExistentTag.someTag)

try:
    badContent = BeautifulSoup(html.read())
    title = bsObj.body.h3
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent==None:
        print("Tag was not found")
    else:
        print(title)


#综合调试程序
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)