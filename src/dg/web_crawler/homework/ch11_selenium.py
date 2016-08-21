# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 23:21:21 2016

@author: lenovo-pc
"""

# Ajax
from selenium import webdriver
import time

driver = webdriver.PhantomJS(
    executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# driver.page_source
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()

# 检查页面是否加载完毕
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(
    executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()

# 重定向
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


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


driver = webdriver.PhantomJS(
    executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
