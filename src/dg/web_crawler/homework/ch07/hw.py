# _*_ coding: utf-8 _*_
from weibo import APIClient
# python内置的包
import webbrowser

APP_KEY = '834896928'
APP_SECRET = '8861043e6a9134bffc42df1810402a24'
CALLBACK_URL = 'http://f.dataguru.cn/'

# 利用官方微博SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
# 得到授权页面的url，利用webbrowser打开这个url
url = client.get_authorize_url()
print url
webbrowser.open_new(url)

# http://f.dataguru.cn/?code=0599cd35cbe9b2935d6ae54f1c2bad49

# 获取code=后面的内容
code = '0599cd35cbe9b2935d6ae54f1c2bad49'

# 获取token
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in  # token过期的UNIX时间

# 设置得到的access_token
client.set_access_token(access_token, expires_in)

# 获取登录用户的关注人信息
# statuses/friends_timeline/ids
statuses = client.statuses.friends_timeline.ids.get(count=10)['statuses']
length = len(statuses)

# 输出了部分信息
print statuses
for i in range(0, length):
    print u'ID：' + statuses[i]

# place/users/show
print client.place.statuses.show.get(uid="4000892796265387")

