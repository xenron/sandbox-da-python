from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pymysql
import re
import datetime
import random

# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
# cur = conn.cursor()
# cur.execute("USE scraping")
# cur.execute("SELECT * FROM pages WHERE id=1")
# print(cur.fetchone())
# cur.close()
# conn.close()

# save wiki links to mysql database
# conn = pymysql.connect(host='192.168.101.81', unix_socket='/tmp/mysql.sock', user='root', passwd='xuran123456', db='mysql', charset='utf8')
conn = pymysql.connect(host='192.168.101.81', user='root', passwd='xuran123456', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE test")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()


def saveLinks(text):
    base_link = "https://en.wikipedia.org"
    html = urlopen(base_link + "/wiki/" + text)
    bsObj = BeautifulSoup(html)
    # print bsObj.prettify()
    pattern = "[" + text + "|" + text.lower() + "]"
    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)(.*" + pattern + ")*$")):
        if 'href' in link.attrs:
            print (link.attrs['href'])


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def test():
    links = getLinks("/wiki/Kevin_Bacon")
    count = 0
    try:
        while len(links) > 0 and count < 100:
            newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
            print(newArticle)
            links = getLinks(newArticle)
            count += 1
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    # saveLinks("Statistics")
    test()
