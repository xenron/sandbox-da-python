# -*- coding: utf-8 -*-

import nltk

# 1. 编写文法，分析以下歧义句子
# 几个工厂的工人
# 他的故事讲不完

# 文法
groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP | NP | AP NP VP
NP -> Det NP | Det AP N | AP N  | N
VP -> V AP | V NP
N -> '校长'|'座谈会'|'工人'|'故事'
Det -> '三个'|'几个'
AP -> '学校的'|'工厂的'|'他的'|'不完'
V -> '参加'|'讲'
""",encoding='utf-8')

# 几个工厂的工人
sent = [u'几个', u'工厂的', u'工人']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.parse(sent)
for tree in trees:
    tree.draw()

# 他的故事讲不完
sent = [u'他的', u'故事', u'讲', u'不完']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.parse(sent)
for tree in trees:
    tree.draw()

# 2. 根据课上的第一个例子（北京是祖国的首都等句子），尝试编写程序，随机构造出符合文法的句子

from nltk.parse.generate import generate

grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V AP | V NP
V -> '是'|'走在'|'进入'
AP -> '很抽象的'
NP -> '北京'|'哈尔滨'|'形式语言'|'中国'|'教育'|'集合'|'WTO'|'美丽的城市'|'祖国的首都'|'数学的基础'|'社会发展的前面'
""",encoding='utf-8')

print(grammar)

for sentence in generate(grammar, n=10):
    print(' '.join(sentence))


