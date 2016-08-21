# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 23:21:21 2016

@author: lenovo-pc
"""


#Ajax
from selenium import webdriver
import time


driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
#driver.page_source
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()

#检查页面是否加载完毕
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
    
    
#重定向
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

driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)

#Pillow 图象处理
from PIL import Image, ImageFilter

kitten = Image.open(u"E:/Python网络爬虫/0.png")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save(u"E:/Python网络爬虫/1.png")
blurryKitten.show()

#规范文字读取
from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    #call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"])
    
    #Open and read the resulting data file
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("D:/Program Files (x86)/Tesseract-OCR/pic2.tif", 
          "D:/Program Files (x86)/Tesseract-OCR/pic3.png")

#从网站中抓取文字
import time
from urllib import urlretrieve
from selenium import webdriver

#driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver = webdriver.Firefox(executable_path=u'C:/Program Files (x86)/Mozilla Firefox/firefox')
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

driver.find_element_by_id("img-canvas").click()
#The easiest way to get exactly one of every page
imageList = set()

#Wait for the page to load
time.sleep(10)
print(driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"))
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    #While we can click on the right arrow, move through the pages
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    #Get any new pages that have loaded (multiple pages can load at once)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

#Start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())


#验证码提取
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html,'lxml')
#Gather prepopulated form values
imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"]
captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"]

captchaUrl = "http://pythonscraping.com"+imageLocation
urlretrieve(captchaUrl, "captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=
    subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "r")

#Clean any whitespace characters
captchaResponse = f.read().replace(" ", "").replace("\n", "")
print("Captcha solution attempt: "+captchaResponse)

if len(captchaResponse) == 5:
    params = {"captcha_token":captchaToken, "captcha_sid":captchaSid,   
              "form_id":"comment_node_page_form", "form_build_id": formBuildId, 
                  "captcha_response":captchaResponse, "name":"Ryan Mitchell", 
                  "subject": "I come to seek the Grail", 
                  "comment_body[und][0][value]": 
                                           "...and I am definitely not a bot"}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10", 
                          data=params)
    responseObj = BeautifulSoup(r.text,'lxml')
    if responseObj.find("div", {"class":"messages"}) is not None:
        print(responseObj.find("div", {"class":"messages"}).get_text())
else:
    print("There was a problem reading the CAPTCHA correctly!")