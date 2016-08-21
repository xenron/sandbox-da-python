# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

# 查找python相关图书
url = "http://search.jd.com/Search?keyword=Python&enc=utf-8"


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


def parse_info_from_soup(bs):
    # 查找所有class为"gl-item"，标签名为li的标签
    items = bs.find_all("li", class_="gl-item")
    # 遍历所有标签
    for item in items:
        # 名称
        # 查找class为"p-name",标签名为div的标签，并查找em内容
        name = item.find("div", class_="p-name").find("em")
        # 价格
        price = item.find("div", class_="p-price").find("i")
        # 出版社
        # book_detail = item.find("span", class_="p-bi-store").find("a")
        # 评论人数
        # commit = item.find("div", class_="p-commit").find("a")
        print(name.text, price.text)
        # print(name.text, book_detail.text, price.text, commit.text)
    # print(len(items))


def main():
    driver = webdriver.PhantomJS(executable_path=r'D:/ProtableSoft/phantomjs-2.1.1-windows/bin/phantomjs')
    driver.get(url)
    waitForLoad(driver)
    bs = BeautifulSoup(driver.page_source)  # 将页面信息转换为BeautifulSoup对象
    parse_info_from_soup(bs)  # 从页面中提取信息
    # print(driver.page_source)


if __name__ == "__main__":
    main()
    # IOLoop.instance().run_sync(main1)
