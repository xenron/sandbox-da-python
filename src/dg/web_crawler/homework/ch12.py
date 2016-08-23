# -*- coding: utf-8 -*-

#修改headers
import requests
from bs4 import BeautifulSoup


#使用selenium测试wiki
from selenium import webdriver

def test1():
    driver = webdriver.PhantomJS(executable_path=r'D:/ProtableSoft/phantomjs-2.1.1-windows/bin/phantomjs')
    driver.get("http://en.wikipedia.org/wiki/Monty_Python")
    try:
        assert len(driver.find_element_by_id("toctitle").text) > 0
        driver.find_elements_by_class_name("navbox-inner")
        print("包含页内导航链接")
        driver.close()
    except AssertionError:
        print("不包含页内导航链接")

def test2():
    driver = webdriver.PhantomJS(executable_path=r'D:/ProtableSoft/phantomjs-2.1.1-windows/bin/phantomjs')
    driver.get("http://en.wikipedia.org/wiki/Monty_Python")
    try:
        assert len(driver.find_elements_by_class_name("navbox-inner")) > 0
        print("包含相关信息链接")
        driver.close()
    except AssertionError:
        print("不包含相关信息链接")


if __name__ == '__main__':
    test1()
    test2()
