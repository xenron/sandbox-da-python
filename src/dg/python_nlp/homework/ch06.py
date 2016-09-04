# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
import nltk
from nltk.corpus import *
from matplotlib import pylab
from nltk import word_tokenize
import re
import jieba
import jieba.posseg
import jieba.analyse
from nltk.corpus import brown
import nltk


# 10. ○ Train a unigram tagger and run it on some new text. Observe that some words are not assigned a tag. Why not?
# 训练一个unigram 标注器，在一些新的文本上运行。观察有些词没有分配到标记。为什么没有？
fd = nltk.FreqDist(brown.words(categories='news'))
# brown_tagged_sents = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.most_common(100)
likely_tags = dict((word, cfd[word].max()) for (word, __) in most_freq_words)
likely_tags
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
brown_tagged_sents=brown.tagged_sents(categories='news')
baseline_tagger.evaluate(brown_tagged_sents)

# Test
# how,you两个单词在高频100单词中未出现，所以没有被标记出来
baseline_tagger.tag([u'how', u'are',u'you'])




















# 20. ◑ Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the following questions:
# a. Produce an alphabetically sorted list of the distinct words tagged as MD.
# b. Identify words that can be plural nouns or third person singular verbs (e.g., deals, flies).
# c. Identify three-word prepositional phrases of the form IN + DET + NN (e.g., in the lab).
# d. What is the ratio of masculine to feminine pronouns?
# 编写代码，搜索布朗语料库，根据标记查找特定的词和短语，回答下列问题：
# a. 产生一个标注为MD的不同的词的按字母顺序排序的列表。
# b. 识别可能是复数名词或第三人称单数动词的词（如deals，flies）。
# c. 识别三个词的介词短语形式IN + DET + NN（如in the lab ）。
# d. 男性与女性代词的比例是多少？

text = brown.words()
tagged_text = brown.tagged_words()
set_text = set(text)
cfd = nltk.ConditionalFreqDist(tagged_text)
conditions = cfd.conditions()

# Q-a
md_words = [condition for condition in conditions if cfd[condition]['MD'] != 0]
md_words.sort()
print(md_words)

# Q-b
two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
two_words.sort()
print(two_words)

# Q-c
tagged_text = brown.tagged_words()
trigrams = list(nltk.trigrams(tagged_text))
for trigram in trigrams:
    zipped_tag = [t for t in zip(*trigram)]
    if zipped_tag[1] == ('IN', 'DT', 'NN'):
        print(zipped_tag[0])

# Q-d
fd = nltk.FreqDist(text)
masc_fem_proportion = (fd['he'] + fd['He']) / (fd['she'] + fd['She'])
print(masc_fem_proportion)


# 22. ◑ We defined the regexp_tagger that can be used as a fall-back tagger for unknown words.
# This tagger only checks for cardinal numbers. 
# By testing for particular prefix or suffix strings, it should be possible to guess other tags. 
# For example, we could tag any word that ends with -s as a plural noun. 
# Define a regular expression tagger (using RegexpTagger()) that tests for at least five other patterns in the spelling of words. 
# (Use inline documentation to explain the rules.)
# 定义可以用来做生词的回退标注器的regexp_tagger。这个标注器只检查基数词。
# 通过特定的前缀或后缀字符串进行测试，它应该能够猜测其他标记。
# 例如：我们可以标注所有-s 结尾的词为复数名词。定义一个正则表达式标注器（使用RegexpTagger()），
# 测试至少5 个单词拼写的其他模式。（使用内联文档解释规则。）
patterns = [
    (r'.*ed$', 'VBD'),  # simple past'
    (r'.*ing$', 'VBG'),  # gerunds end in 'ing'
    (r'.*s$', 'NNS'),  # plural noun
    (r'.*\'s', 'NN$'),  # possessive
    (r'.*', 'NN')  #
]

brown_sents = brown.sents(categories='news')
regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))


# 36. ● Create a regular expression tagger and various unigram and n-gram taggers, incorporating backoff, and train them on part of the Brown Corpus.
# a. Create three different combinations of the taggers. Test the accuracy of each combined tagger. Which combination works best?
# b. Try varying the size of the training corpus. How does it affect your results?
# 创建一个正则表达式标注器和各种unigram 以及n-gram 标注器，包括回退，在布朗语料库上训练它们。
# a. 创建这些标注器的3 种不同组合。测试每个组合标注器的准确性。哪种组合效果最好？
# b. 尝试改变训练语料的规模。它是如何影响你的结果的？
tagged_sents = brown.tagged_sents(categories='news')

size = int(len(tagged_sents) * 0.99)
train_sents = tagged_sents[:size]
test_sents = tagged_sents[size:]

patterns = [
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ed$', 'VBD'),  # simple past
    (r'.*es$', 'VBZ'),  # 3rd singular present
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'NN$'),  # possessive nouns
    (r'.*s$', 'NNS'),  # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')  # nouns (default)
]

t0 = nltk.DefaultTagger('NN')
tr = nltk.RegexpTagger(patterns, backoff=t0)
t1 = nltk.UnigramTagger(train_sents, backoff=tr)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.evaluate(test_sents))

