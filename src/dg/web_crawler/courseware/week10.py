# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 13:47:00 2016

@author: Administrator
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

###获取n-gram
def getNgrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,'lxml')
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))


#转义字符清除
def ngrams(input,n):
    content=re.sub('\n+',' ',input)
    content=re.sub(' +',' ',content)
    content=content.encode('ascii','ignore')
    print content
    input = content.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

ngrams = ngrams(content, 2)
print(ngrams)

#增加过滤规则
def cleanInput(input):
#    input = input.lower()
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = input.encode('ascii','ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)



ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)


####自然语言分析####
#数据概况
import operator
def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = input.encode('ascii','ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output
    
content = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read().encode('utf-8')
ngrams = getNgrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)

#过滤无意义n-gram
def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

def cleanText(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub("u\.s\.", "us", input)
    input = input.encode('ascii','ignore')
    return input

def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read().encode('utf-8')
ngrams = getNgrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse = True)
print(sortedNGrams)


#马尔可夫模型
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):

    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #剔除换行符和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")

    #保证每个标点都和前面的单词在一起，保留在马尔可夫链中
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text = text.replace(symbol, " "+symbol+" ")

    words = text.split(" ")
    #过滤空单词
    words = [word for word in words if word != ""]

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #为单词新建一个词典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1

    return wordDict

text = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read().encode('utf-8')
wordDict = buildWordDict(text)

#生成长度为100的马尔可夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord+" "
    #print(wordDict[currentWord])
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)


##NLTK包
import nltk
nltk.download()

from nltk.book import  *

###搜索文本
#搜索单词
text1.concordance("monstrous")
text2.concordance("affection")
text3.concordance("lived")
text5.concordance("lol")

#搜索相似词
text1.similar("monstrous")

text2.similar("monstrous")

#搜索共同上下文
text2.common_contexts(["monstrous", "very"])

#词汇分布图
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

#自动生成文章
text3.generate()

###计数词汇
len(text3)

sorted(set(text3))

len(set(text3))

#重复词密度
from __future__ import division
len(text3) / len(set(text3))

#关键词密度
text3.count("smote")

100 * text4.count('a') / len(text4)

def lexical_diversity(text): 
    return len(text) / len(set(text)) 
    
def percentage(count, total): 
    return 100 * count / total
    
lexical_diversity(text3)

lexical_diversity(text5)

percentage(4, 5)

percentage(text4.count('a'), len(text4))




###简单统计
saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:]

#频率分布
fdist1 = FreqDist(text1)
fdist1

vocabulary1 = fdist1.keys()
vocabulary1[:50]

fdist1['whale']

fdist1.plot(50, cumulative=True)

fdist1.hapaxes()

#细粒度的选择词
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

V = set(text5)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

fdist5 = FreqDist(text5)
sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])

#词语搭配
from nltk.util import bigrams
list(bigrams(['more', 'is', 'said', 'than', 'done']))

text4.collocations()

text8.collocations()




