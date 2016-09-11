# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
# import MySQLdb
import time
import sqlite3
import itertools
import os

TIME_INTERVAL = 10  # 时间间隔

# conn = MySQLdb.connect(host="xxxxx", user="xxxxx", passwd="xxxxx", db="xxxxx", charset="utf8")
# conn.autocommit(1)
# cursor = conn.cursor()
conn = sqlite3.connect('output.sqllite3')
cursor = conn.cursor()
# conn.execute('''CREATE TABLE rating
#     (user_id TEXT     ,
#     movie_id           TEXT    ,
#     movie_name            TEXT     ,
#     movie_rating        TEXT,
#     movie_date         TEXT);''')

'''
------------------------------------
函数名：InsertDatabase
输入参数：
user_id：用户ID
movie_id：电影ID
movie_rating：电影评分
movie_data：评分日期
------------------------------------
'''


def InsertDatabase(user_id, movie_id, movie_name, movie_rating, movie_date):
    global cursor
    # sql = "insert into rating (user_id,movie_id,movie_name,movie_rating,movie_date) values(%s,%s,%s,%s,%s)"
    # param = (user_id, movie_id, movie_name, movie_rating, movie_date)
    # res = cursor.execute(sql, param)
    sql = "insert into rating (user_id,movie_id,movie_name,movie_rating,movie_date) values('" + user_id + "' , '" + movie_id + "' , '" + movie_name + "' , '" + movie_rating + "' , '" + movie_date + "' ) "
    print(sql)
    conn.execute(sql)


'''
------------------------------------
函数名：isUserExist
函数说明：查找数据库，返回是否存在这个用户，存在返回True，否则返回False
输入参数：
    user_id：用户ID
------------------------------------
'''


def isUserExist(user_id):
    global cursor
    sql = "select count(*) from rating where user_id = " + "'" + user_id + "'"
    cursor.execute(sql)
    res = cursor.fetchall()
    if res[0][0] > 0:
        return True
    else:
        return False


'''
------------------------------------
函数名：GetUserList
函数说明：获取用户的ID表
输入参数：
    num：要获取用户的个数
    movie_id：从哪个电影的页面中获取
返回值
    ret_list：包含用户ID的一个List
------------------------------------
'''


def GetUserList(movie_id, num=25):
    ret_list = []  # 要返回的用户列表
    count = 0  # 用户数
    next_page_link = ""  # 下一页的链接
    while count <= num:  # 如果用户数不足的话，继续找
        if count == 0:
            url = "http://movie.douban.com/subject/" + movie_id + "/comments?start=0&limit=20&sort=new_score"
        else:
            url = next_page_link
        request = urllib2.Request(url, headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })  # 注意构造Header，否则可能会被服务器识别为爬虫程序
        response = urllib2.urlopen(request)
        page = BeautifulSoup(response, "html.parser")  # 获取页面
        comment_list = page.find_all(class_="comment-item")  # 找到所有用户
        for item in comment_list:
            if item.div.a:
                user_link = "%s" % item.div.a.get("href")
                if "people" in user_link:  # 确认是否是用户链接
                    user_id = user_link.split('/')[-2]  # 获取用户id
                    if not isUserExist(user_id):
                        ret_list.append(user_id)  # 加入列表中
                        count += 1
                        print "Found the user: %s" % user_id
                        if count > num:
                            break

        next_page = page.find(class_="next")  # 查找下一页
        if next_page:
            next_page_link_tmp = "%s" % next_page.get("href")
            next_page_link = "http://movie.douban.com/subject/" + movie_id + "/comments" + next_page_link_tmp
        else:
            break

        time.sleep(TIME_INTERVAL)  # 暂停运行，防止爬虫速度过快致使被豆瓣封IP
    return ret_list  # 返回用户表


'''
------------------------------------
函数名：GetUserRating
函数说明：获取用户的评分
输入参数：
    user_id：用户的ID
------------------------------------
'''


def GetUserRating(user_id):
    count = 0
    url = "http://movie.douban.com/people/" + user_id + "/collect?start=0&sort=rating&rating=all&filter=all&mode=list"

    is_continue = True  # 判断是否继续
    error_count = 0

    while is_continue:
        request = urllib2.Request(url, headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })

        response = urllib2.urlopen(request)
        page = BeautifulSoup(response.read(), "html.parser")

        list_view = page.find(class_="list-view")
        rating_list = list_view.find_all("li")
        for item in rating_list:
            if not item.div.div.a:
                continue
            movie_name = "%s" % item.div.div.a.string  # 获取电影名字
            movie_name = movie_name.strip()
            if item.div.div.a.get("href"):
                movie_id_tmp = "%s" % item.a.get("href")
                movie_id = movie_id_tmp.split('/')[-2]

            span_list = item.div.find_all("span")
            date_div = item.find(class_="date")
            movie_rating = ""
            movie_date = ""
            for span in span_list:
                if "rating" in "%s" % span.get("class"):
                    movie_rating = "%s" % span.get("class")
                    movie_rating = movie_rating[9]
            movie_date = "%s" % date_div.getText()
            movie_date = movie_date.strip()
            if movie_rating == "":
                is_continue = False
                break
            else:
                count += 1
                # print "%4d %3s %13s %s"%(count,movie_rating,movie_date,movie_name)
                InsertDatabase(user_id, movie_id, movie_name, movie_rating, movie_date)

        page_next = page.find(class_="next")

        # 如果没有下一页的话
        if not page_next:
            is_continue = False
        else:
            if page_next.find("a"):
                url = "%s" % page_next.find("a").get("href")
            else:
                is_continue = False
        time.sleep(TIME_INTERVAL)  # 休息


def main():
    user_list = GetUserList("1292052", 20)
    for user_id in user_list:
        print "The user_id is : %s" % user_id
        GetUserRating(user_id)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
