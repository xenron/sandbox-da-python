# import nltk
# nltk.download()

from nltk import FreqDist
# from nltk.book import text5
from nltk.book import *


def question01():
    print(len(text2))
    print(len(set(text2)))


def question02():
    print(text2[-2:])


def getNgrams(input, n):
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output


def question03():
    ngrams = getNgrams(text5, 2)
    print(ngrams)
    print("2-grams count is: " + str(len(ngrams)))


if __name__ == '__main__':
    print("\n========= question01 =========")
    question01()
    print("\n========= question02 =========")
    question02()
    print("\n========= question03 =========")
    question03()
    print("\n========= finish =========")
