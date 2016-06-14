说明：

1，a.txt--存放数据抓取结果，请修改settings.py中的FEED_URI为本地路径

2，修改bioospider.py中的用户名(account,username)、密码(password)为自己注册的用户名、密码

3, 修改def closed(self,reason)：方法，把to和cc参数修改为要发送到的邮箱、要抄送到的邮箱

4，修改setting.py中的参数 MAIL_FROM、MAIL_USER、MAIL_PASS 