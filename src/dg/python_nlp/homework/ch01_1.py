import time


def check_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print('year : ' + str(year) + ' is a leap year')
    else:
        print('year : ' + str(year) + ' is not a leap year')


if __name__ == '__main__':
    # 获取年份
    thisyear = time.localtime()[0]
    check_leap_year(thisyear)
    check_leap_year(1900)
    check_leap_year(2000)
    check_leap_year(2008)

