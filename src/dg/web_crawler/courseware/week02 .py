
# coding: utf-8

# In[16]:

import urllib2
import urllib
 
response = urllib2.urlopen("http://www.baidu.com")
print response.read()


# In[17]:

print response


# In[18]:

#构造Request
request = urllib2.Request("https://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()


# In[19]:

#post方式
values = {"username":"Python爬虫","password":"123456789"}
data = urllib.urlencode(values) 
url = "http://www.dataguru.cn/member.php?mod=logging&action=login"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()


# In[20]:

#post方式的另一种写法
values = {}
values['username'] = "python爬虫"
values['password'] = "123456789"
data = urllib.urlencode(values) 
url = "http://www.dataguru.cn/member.php?mod=logging&action=login"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()


# In[21]:

#get方式
values={}
values['username'] = "python爬虫"
values['password']="123456789"
data = urllib.urlencode(values) 
url = "http://www.dataguru.cn/member.php"
geturl = url + "?"+data
print geturl
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()


# In[29]:

#设置headers
url = 'http://www.baidu.com'
request=urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response = urllib2.urlopen(request)  
page = response.read() 
print response.getcode()
print len(page)
print page


# In[39]:

url = 'http://www.dataguru.cn/member.php?mod=logging&action=login'
user_agent = 'Mozilla/5.0'  
values = {'username' : 'python爬虫',  'password' : '123456789' }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
request.add_header("user-agent","Mozilla/5.0")
request.add_data(data)
response = urllib2.urlopen(request)  
page = response.read() 
print page


# In[40]:

#代理设置

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


# In[41]:

#timeout设置
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
#response = urllib2.urlopen('http://www.baidu.com',data, 10)


# In[43]:

#debuglog的使用

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


# In[44]:

#获取cookies
import cookielib

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


# In[45]:

#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)


# In[46]:

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()


# In[48]:

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'username':'python爬虫',
            'pwd':'123456789'
        })
#登录dataguru的URL
loginUrl = 'http://www.dataguru.cn/member.php?mod=logging&action=login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是Python网络爬虫的网址
gradeUrl = 'http://www.dataguru.cn/myclassnew.php?mod=new_basicforlesson&op=basic&lessonid=773'
#请求访问Python网络爬虫首页
result = opener.open(gradeUrl)
print result.read()


# In[49]:

#URLError
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason


# In[50]:

#HTTPError
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason


# In[51]:

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"


# In[52]:

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"




