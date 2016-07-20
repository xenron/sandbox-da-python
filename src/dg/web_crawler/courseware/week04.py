# -*- coding: utf-8 -*-
import re

s='123abc456eabc789'
re.findall(r'abc',s)

#限定符
s='Chapter1 Chapter2 Chapter10 Chapter99 fheh'
re.findall('Chapter[1-9][0-9]*', s)
re.findall('Chapter[1-9]{1,2}', s)
re.findall('Chapter[1-9][0-9]?', s)
re.findall('Chapter[1-9][0-9]{0,1}', s)

s='<H1>Chapter 1 – Introduction to Regular Expressions</H1>'
re.findall('<.*>',s)
re.findall('<.*?>',s)

#定位符
s='Chapter1 Chapter2 Chapter11 Chapter99'
re.findall('^Chapter[1-9][0-9]{0,1}',s)
re.findall('^Chapter[1-9][0-9]{0,1}$','Chapter99')

re.findall(r'\bCha',' Chapter')
re.findall(r'ter\b',' Chapter')
re.findall(r'\Bapt','Chapter')
re.findall(r'\Bapt','aptitude')

#选择与无捕获组
s = 'I have a dog , I have a cat'
re.findall( r'I have a (?:dog|cat)' , s )

re.findall( r'I have a dog|cat' , s )

s='ababab abbabb aabaab'
re.findall(r'\b(?:ab)+\b', s )

re.findall(r'\b(ab)+\b', s )

#组
s = 'aaa111aaa , bbb222 , 333ccc'
re.findall (r'[a-z]+(\d+)[a-z]+' , s )

s='aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
re.findall( r'([a-z]+)\d+([a-z]+)' , s )
re.findall( r'(?P<g1>[a-z]+)\d+(?P=g1)' , s )
re.findall( r'[a-z]+(\d+)([a-z]+)' , s )
re.findall( r'([a-z]+)\d+' , s )
re.findall( r'([a-z]+)\d+\1' , s )

s='111aaa222aaa111 , 333bbb444bb33'
re.findall( r'(\d+)([a-z]+)(\d+)(\2)(\1)' , s )

#反向引用
s='Is is the cost of of gasoline going up up ?'
re.findall(r'\b([a-z]+) \1\b',s,re.I)

s='http://www.w3cschool.cc:80/html/html-tutorial.html'
re.findall(r'(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)',s)

#基本匹配模式
s1="once upon a time"
s2="There once was a man from NewYork"
print re.findall(r'^once',s1)
print re.findall(r'^once',s2)

print re.findall(r'time$',s1)
print re.findall(r'times$',s1)

print re.findall(r'^time$',s1)
print re.findall(r'^time$','time')

s='''There once was a man from NewYork
Who kept all of his cash in a bucket.'''
print re.findall(r'once',s)

#compile
s='111,222,aaa,bbb,ccc333,444ddd'
rule=r'\b\d+\b'
compiled_rule=re.compile(rule)
compiled_rule.findall(s)

#match
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

#search
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"


#match与search
line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

#sub
phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num

#正则表达式与BeautifulSoup
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.prettify())
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images: 
    print(image["src"])
