# -*- coding: utf-8 -*-
import requests
import json

#####Requests的用法#####
#url下载
r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies

#基本请求
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")

#get请求
r = requests.get("http://httpbin.org/get")

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url


r = requests.get('https://github.com/timeline.json', stream=True)
r.raw


payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print r.url

#post请求
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text

url = 'http://httpbin.org/post'
files = {'file': open('d:/data/test.txt', 'rb')}
r = requests.post(url, files=files)
print r.text


#Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text


#超时配置
requests.get('http://github.com', timeout=0.001)

#会话对象
requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text

r = s.get('http://httpbin.org/headers', headers={'x-test': 'true'})

r = s.get('http://httpbin.org/headers', headers={'x-test': None})

#SSL证书验证
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print r.text

r = requests.get('https://github.com', verify=True)
print r.text

r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text

#代理
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text


export HTTP_PROXY="http://10.10.1.10:3128"
export HTTPS_PROXY="http://10.10.1.10:1080"


#####BeautifulSoup的用法#####
import urllib2
import bs4
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

#CSS属性
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

#find()和findall()
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
allText = bsObj.findAll(id="text")
print(allText[0].get_text())

#创建HTML对象
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
print soup.prettify()

#name参数
soup.find_all('b')


import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

soup.find_all(["a","b"])

for tag in soup.find_all(True):
    print(tag.name)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)

#keyword参数
soup.find_all(id='link2')

soup.find_all(href=re.compile("elsie"))

soup.find_all(href=re.compile("elsie"),id='link1')

soup.find_all("a",class_="sister")

data_soup=BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo='value')

data_soup.find_all(attrs={"data-foo":"value"})

#text参数
soup.find_all(text="Elsie")
# [u'Elsie']
 
soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']
 
soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]

#limit参数
soup.find_all("a",limit=2)

#recursive参数
soup.html.find_all("title",recursive=False)

#tag对象
print soup.title
print soup.head
print soup.a
print soup.p

print type(soup.a)

print soup.name
print soup.head.name

print soup.p.attrs

print soup.p['class']

print soup.p.get('class')

soup.p['class']="newclass"
print soup.p

del soup.p['class']
print soup.p

#NavigableString对象
print soup.p.string

print type(soup.p.string)

#BeautifulSoup对象
print type(soup.name)
print soup.name
print soup.attrs

#comment对象
print soup.a
print soup.a.string
print type(soup.a.string)

if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
    
###导航树
#直接子节点
print soup.body.contents

for child in soup.body.children:
    print(child)

#所有后代节点

for child in soup.descendants:
    print child

#节点内容
for string in soup.strings:
    print(repr(string))


for string in soup.stripped_strings:
    print(repr(string))

#兄弟节点
print soup.p.next_sibling
#       实际该处为空白
print soup.p.prev_sibling
#None   没有前一个兄弟节点，返回 None
print soup.p.next_sibling.next_sibling

for sibling in soup.a.next_siblings:
    print(repr(sibling))

#前后节点
print soup.head.next_element
    
#父节点
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print bsObj.prettify()
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

###CSS选择器
print soup.select('title')
print soup.select('a')
print soup.select('b')

print soup.select('.sister')

print soup.select('#link1')

print soup.select('p #link1')
print soup.select('head > title')

print soup.select('a[class="sister"]')

print soup.select('a[href="http://example.com/elsie"]')

print soup.select('p a[href="http://example.com/elsie"]')


print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()
