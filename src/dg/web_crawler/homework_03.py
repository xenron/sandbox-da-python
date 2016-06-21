from urllib2 import urlopen
from bs4 import BeautifulSoup


def test01():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll("span", {"class":"red"})
    for name in nameList:
        print(name.get_text())


def test02():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    
    for child in bsObj.find("table",{"id":"giftList"}).children:
        if len(child) == 4:
            print(child.td)


def test03():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    
    for child in bsObj.find("table",{"id":"giftList"}).children:
        if len(child) == 4:
            print(child.select('td')[0].get_text())


if __name__ == '__main__':
    # test01()
    test02()
    # test03()
