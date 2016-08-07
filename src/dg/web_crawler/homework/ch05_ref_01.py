from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
html = urlopen("https://en.wikipedia.org/wiki/Statistics")
bsObj = BeautifulSoup(html)
print bsObj.prettify()
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)(.*[Ss]tatistics)*$")):
    if 'href' in link.attrs:
        print (link.attrs['href'])