# coding: utf-8
import json
import os
from time import sleep

import MySQLdb
from maizi.settings import *
import requests
from multiprocessing import Pool, Manager

# 打开数据库连接

def dbconnect():
    try:
        db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME, charset="utf8")
        return  db
    except Exception:
        print("db connect error!\n the err msg :%s" % Exception.message)
        return None
# update excute
def excutesql(sql):
    db = dbconnect()
    if db is None:
        return
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        print("execute error!\n the err msg :%s" % Exception.message)
        db.rollback()
    finally:
        cursor.close()
        db.close()
# get_data
# return a dict list
def excute_featch(sql):
    data_list=[]
    db = dbconnect()
    if db is None:
        return
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        revs= cursor.fetchall()
        for row in revs:
            pass
    except Exception:
        print("execute error!\n the err msg :%s" % Exception.message)
    finally:
        cursor.close()
        db.close()

def get_db_data():
    data_lists = []
    db = dbconnect()
    if db is None:
        return
    cursor = db.cursor()
    sql = "SELECT * FROM course WHERE course.IsDown = '0' ORDER BY course.id ASC"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            data = {}
            data['LessID'] = row[1]
            data['LessName'] = row[2]
            data['LessHref'] = row[3]
            data['LessVideo'] = row[4]
            data['pLessID'] = row[5]
            data['pLessName'] = row[6]
            data['pLessHref'] = row[7]
            data['IsDown'] = row[8]
            # print "%(LessID)s %(LessName)s %(LessHref)s %(LessVideo)s %(pLessID)s %(pLessName)s %(pLessHref)s %(IsDown)s " % data
            data_lists.append(data)
        db.close()
    except Exception:
        print(Exception.message)
        print "Error: unable to fecth data"
    return data_lists
def parse_josn():
    data_lists = []
    mzjson = open("mz.json", "r")
    for item in mzjson:
        data = json.loads(item)
        try:
            data_lists.append(data)
        except:
            pass
    return data_lists
    mzjson.close()


def create_path(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return path

def update_status(data):
    db= dbconnect()
    cursor = db.cursor()
    sql = "UPDATE course SET IsDown = '1' WHERE LessID = '%s'" % (data['LessID'])
    try:
       cursor.execute(sql)
       db.commit()
    except:
        print("the video:%(LessName)s id update falier!" % data)
        db.rollback()
    db.close()

def downLoad(data):
    r = requests.get(data["LessVideo"])
    base_path = create_path("e://bootstrap//"+data["pLessName"]+"//")
    video = base_path + data["LessName"] + ".mp4"
    # print(video)
    try:
        with open(video, "wb") as code:
            code.write(r.content)
        # update_status(data)
        print(video + " is down load success!")
    except Exception:
        print("the down video:%(LessName)s load is failer\n url is :%(LessHref)s \n videourl:%(LessVideo)s " % data)
        print(Exception.message)
        pass
if __name__=="__main__":
    pool = Pool(16)
    datas = get_db_data()
    pool.map(downLoad,datas)
    pool.close()
    pool.join()
