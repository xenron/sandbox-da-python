# _*_ coding: utf-8 _*_
from weibo import APIClient
import webbrowser

APP_KEY = ''
APP_SECRET = ''
CALLBACK_URL = ''
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