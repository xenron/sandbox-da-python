from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

def validateEmail(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    return False


def validateURL(url):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", url) != None:
        return True
    return False


def validateHtmlTag(tag, target):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", tag) != None:
        return True
    return False


def validateInteger(integer):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", integer) != None:
        return True
    return False


if __name__ == '__main__':
    print(validateEmail("abc@test.com"))
    print(validateEmail("abc#test.com"))
    print(validateURL("abc#test.com"))
    print(validateHtmlTag("abc#test.com", "<img>"))
    print(validateInteger("1"))
