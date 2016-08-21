# import nltk
# nltk.download()

from nltk import FreqDist
# from nltk.book import text5
from nltk.book import *


def question04():
    # print(text2.plot())
    print(len(text2))
    print(len(set(text2)))


def question07():
    text5.collocations()


def question22():
    word_li = [w for w in text5 if len(w) == 4]
    # print(word_li)
    fdist = FreqDist(word_li)
    sorted_word_li = sorted(fdist.keys(), key=lambda x: fdist[x], reverse=True)
    for w in sorted_word_li:
        print "%s\t%d; " % (w, fdist[w]),


def question28(word, text):
    freq = len([w for w in text if w == word]) * 1.0 / len(text)
    print("%.2f" % freq)


if __name__ == '__main__':
    print("\n========= question04 =========")
    question04()
    print("\n========= question07 =========")
    question07()
    print("\n========= question22 =========")
    question22()
    print("\n========= question28 =========")
    question28("that", text5)
    print("\n========= finish =========")

