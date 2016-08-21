from nltk.corpus import wordnet as wn
import nltk
from nltk.corpus import *
from matplotlib import pylab

def question02():
    austen = gutenberg.words('austen-persuasion.txt')
    print(len(map(lambda x: x.lower(), austen)))
    print(len(set(map(lambda x: x.lower(), austen))))


def question08():
    cfd = nltk.ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
        for name in names.words(fileid))
    cfd.plot()


def question09():
    pass

def question15():
    print((lambda x: x in brown.words() and brown.words().count(x) >= 3, brown.words()))


def question17(words):
    content = [w for w in words if w.lower() not in stopwords.words('english')]
    print(content)
    print(nltk.FreqDist(content).most_common(50))

if __name__ == '__main__':
    print("\n========= question02 =========")
    question02()
    print("\n========= question08 =========")
    question08()
    print("\n========= question15 =========")
    question15()
    print("\n========= question17 =========")
    question17(["this", "is", "a", "book", "that", "is", "an", "math", "book"])
    print("\n========= finish =========")
