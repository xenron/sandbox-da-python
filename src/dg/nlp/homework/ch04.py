# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
import nltk
from nltk.corpus import *
from matplotlib import pylab
from nltk import word_tokenize
import re


def question02():
    word_1 = 'dishes'
    word_2 = 'running'
    word_3 = 'nationality'
    word_4 = 'undo'
    word_5 = 'preheat'
    print(word_1[:-2])
    print(word_2[:-4])
    print(word_3[:-5])
    print(word_4[:-2])
    print(word_5[:-4])


def question06():
    # 字母字符串
    nltk.re_show('[a-zA-Z]+', 'test123test')
    # 首字母大写
    nltk.re_show('[A-Z][a-z]*', 'Apple123Orange')
    # p开头，t结尾，中间有<=2个元音字母
    nltk.re_show('p[aeiou]{,2}t', 'poat123put')
    # 小数部分可有可无
    # 整数部分一定要有一个或多个数字
    nltk.re_show('\d+(\.\d+)?', '123test123.45')
    # 首尾字母不包含元音，中间有一个元音
    nltk.re_show('([^aeiou][aeiou][^aeiou])*', 'put123cat')
    # 一个或者多个字母
    # 或者，多个非字母非空格
    nltk.re_show('\w+|[^\w\s]+', 'test')
    nltk.re_show('\w+|[^\w\s]+', '123')


def question17():
    # 右对齐
    print('%6s' % 'dog')
    print('%6s' % 'sdasdasdsds')
    # 左对齐
    print('%-6s' % 'dog')
    print('%-6s' % 'sdasdasdsds')


def question24(text):
    """converts a text to hacker"""
    new_text = []

    # initial pass subsitutes 8 for ate.
    pattern = re.compile(r'ate')
    text = pattern.sub('8', text)

    # regex that searches through the text to find instances of the letters to be converted.
    pattern = re.compile(r'[eiols]|\.')

    # converts all the letters
    for w in text:
        if re.search(pattern, w):
            if w == 'e':
                w = '3'
            elif w == 'i':
                w = '1'
            elif w == 'o':
                w = '0'
            elif w == 's':
                w = '5'
            elif w == 'l':
                w = '|'
            elif w == '.':
                w = '5w33t!'
        new_text.extend(w)
    new_text = ''.join(new_text)

    # regex searching for word initial s.
    pattern = re.compile(r'\b5')
    new_text = pattern.sub('$', new_text)

    return new_text


if __name__ == '__main__':
    print("\n========= question02 =========")
    question02()
    print("\n========= question06 =========")
    question06()
    print("\n========= question17 =========")
    question17()
    print("\n========= question24 =========")
    # reads in a text
    f = open('../data/corpus.txt')
    raw = f.read()
    # lower cases the text
    raw = raw.lower()
    print(question24(raw))
    print("\n========= finish =========")
