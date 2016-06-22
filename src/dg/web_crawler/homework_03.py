from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

def test01():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll("span", {"class":"red"})
    for name in nameList:
        print(name.get_text())


def test02():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    # print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
    # print(bsObj.find("img",{"src":re.compile('../img/gifts/img\d.jpg')}).parent.previous_sibling.get_text())
    for node in bsObj.find_all("img",{"src":re.compile('../img/gifts/img\d.jpg')}):
        title = node.parent.previous_sibling.previous_sibling.previous_sibling.get_text()
        cost = node.parent.previous_sibling.get_text()
        print('title : ' + title + 'cost : ' + cost)
    # print(bsObj.find("img").parent.previous_sibling.get_text())
    # print(bsObj.find("table",{"id":"giftList"}))
    # print(bsObj.find("table",{"id":"giftList"}).prettify())
    # for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    #     print(sibling)
    # for child in bsObj.find("table",{"id":"giftList"}).children:
    #     # index = 1
    #     # if len(child) == 4:
    #         print('------------------------')
    #         # print(index)
    #         # index = index + 1
    #         print(type(child))
    #         print(child)
    #         # print(child.tr)
    #         # print(child.th)
    #         # print(child.td)


def test03():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    # print(bsObj.find('td', text = re.compile('Dead Parrot')).parent)
    print(bsObj.find('td', text = re.compile('Dead Parrot')).next_sibling.next_sibling.get_text())
    # for node in bsObj.find('td', text = re.compile('Dead Parrot')):
    #     cost = node.parent.previous_sibling
    #     print('cost : ' + cost)


if __name__ == '__main__':
    # test01()
    # test02()
    test03()
