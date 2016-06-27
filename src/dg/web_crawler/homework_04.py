import re

def validateEmail(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    return False


def validateURL(url):
    if re.match(r'^https?:/{2}\w.+$', url) != None:
        return True
    return False


def validateHtmlImg(tag):
    if re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""",re.I) != None:
        return True
    return False


def validateInteger(integer):
    if re.match("^\+?[0-9]+$", integer) != None:
        return True
    return False


if __name__ == '__main__':
    print("validateEmail")
    print(validateEmail("abc@test.com"))
    print(validateEmail("abc#test.com"))
    print("validateURL")
    print(validateURL("http://a.test.com/"))
    print(validateURL("a.test.com"))
    print("validateHtmlTag")
    print(validateHtmlImg('<img src="icon.png">'))
    print(validateHtmlImg('<input value="icon.png" />'))
    print("validateInteger")
    print(validateInteger("1"))
    print(validateInteger("+1"))
    print(validateInteger("-1"))
