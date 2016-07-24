# _*_ coding: utf-8 _*_
from weibo import APIClient
import webbrowser
import os
import sys
import weibo
import webbrowser
import json

def test01():
    
    APP_KEY = '834896928'
    APP_SECRET = '8861043e6a9134bffc42df1810402a24'
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
    #这个是设置回调地址，必须与那个”高级信息“里的一致
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    # TODO: redirect to url
    #print url
    webbrowser.open_new(url)
    # 获取URL参数code:
    code = '2fc0b2f5d2985db832fa01fee6bd9316'
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # TODO: 在此可保存access token
    client.set_access_token(access_token, expires_in)
    
    print client.friendships.friends.bilateral.ids.get(uid = 12345678)
    
def test02():
    APP_KEY = '834896928'
    MY_APP_SECRET = '8861043e6a9134bffc42df1810402a24'
    REDIRECT_URL = 'http://f.dataguru.cn/'
    #这个是设置回调地址，必须与那个”高级信息“里的一致
    
    #请求用户授权的过程
    client = weibo.APIClient(APP_KEY, MY_APP_SECRET)
    
    authorize_url = client.get_authorize_url(REDIRECT_URL)
    
    #打开浏览器，需手动找到地址栏中URL里的code字段
    webbrowser.open(authorize_url)
    
    #将code字段后的值输入控制台中
    code = raw_input("input the code: ").strip()
    
    #获得用户授权
    request = client.request_access_token(code, REDIRECT_URL)
    
    #保存access_token ,exires_in, uid
    access_token = request.access_token
    expires_in = request.expires_in
    uid = request.uid
    
    #设置accsess_token，client可以直接调用API了
    client.set_access_token(access_token, expires_in)
    
    #get_results = client.statuses__mentions()
    #get_results = client.frientdships__friends__ids()
    #get_results = client.statuses__user_timeline()
    #get_results = client.statuses__repost_timeline(id = uid)
    #get_results = client.search__topics(q = "笨NANA")
    get_results = client.statuses__friends_timeline()
    print "************the type of get_results is : "
    print type(get_results)
    #print get_results[0][0]['text']
    get_statuses = get_results.__getattr__('statuses')
    print type(get_statuses)
    print get_statuses[0]['text']
    
    json_obg = json.dumps(get_results)
    print type(json_obg)
    #resultsdic = json.load(json_obg)
    
    print uid
    
    # get_json = json.dumps(client.statuses__user_timeline())
    #decodejson = json.loads(get_results)
    #print decodejson
    
    #file = open("result.txt", "w")
    #file.write(decodejson)
    #file.close()
    print "*************OK**********"

if __name__ == '__main__':
    # test01()
    test02()