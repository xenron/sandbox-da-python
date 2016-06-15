# coding: utf-8
import json
import os
from time import sleep

import MySQLdb
from maizi.settings import *
import requests
from multiprocessing import Pool, Manager

# 打开数据库连接
db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME, charset="utf8")


def get_db_data():
    data_lists = []
    cursor = db.cursor()
    sql = "SELECT * FROM course WHERE course.IsDown = '0' ORDER BY course.id ASC LIMIT 0, 10"
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
    cursor = db.cursor()
    sql = "UPDATE course SET IsDown = '1' WHERE LessID = '%s'" % (data['LessID'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def downLoad(data):
    r = requests.get(data["video"])
    base_path = create_path("e://bootstrap//" + data["pLessName"] + "//")
    video = base_path + data["Leesion"] + ".mp4"
    # print(video)
    try:
        with open(video, "wb") as code:
            code.write(r.content)
        update_status(data)
        print(video + " is down load success!")
    except Exception:
        print("the down load is failer")
        print(Exception.message)
        pass


# 写数据进程执行的代码:
# def write(q, lock):
#     while (q.full()==False):
#         lock.acquire()  # 加上锁
#         datas = get_db_data()
#         if len(datas)==0:
#             break
#         for data in datas:
#             if q.full():
#                 break
#             q.put(data)
#         lock.release()  # 释放锁
#         sleep(10)
# 写数据进程执行的代码:
def write(q, lock):
    lock.acquire()  # 加上锁
    datas = get_db_data()
    for data in datas:
        if q.full():
            break
        q.put(data)
    lock.release()  # 释放锁

# 读数据进程执行的代码:
def downLoad_by_queue(q):
    while True:
        print('q.qsize():',q.qsize())
        if q.empty():
            print('break!')
            break
        data = q.get(False)
        print(data)
        r = requests.get(data["video"])
        base_path = create_path("e://bootstrap//" + data["pLessName"] + "//")
        video = base_path + data["Leesion"] + ".mp4"
        # print(video)
        try:
            with open(video, "wb") as code:
                code.write(r.content)
            update_status(data)
            print(video + " is down load success!")
        except Exception:
            print("the down load is failer")
            print(Exception.message)
            pass

if __name__ == "__main__":
    pnum = 8
    pool = Pool(pnum)
    result = []
    manager = Manager()
    queue = manager.Queue()
    # 父进程创建Queue，并传给各个子进程：
    lock = manager.Lock()  # 初始化一把锁
    for i in range(pnum):
        pw = pool.apply_async(write, args=(queue, lock))
        sleep(1)
        pr = pool.apply_async(downLoad_by_queue, args=(queue,))
        pool.close()
        pool.join()

