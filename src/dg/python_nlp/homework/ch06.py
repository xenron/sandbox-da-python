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
def q10():
    fd = nltk.FreqDist(brown.words(categories='news'))
    # brown_tagged_sents = nltk.FreqDist(brown.words(categories='news'))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    most_freq_words = fd.most_common(100)
    likely_tags = dict((word, cfd[word].max()) for (word, __) in most_freq_words)
    baseline_tagger = nltk.UnigramTagger(model=likely_tags)
    baseline_tagger.evaluate(brown_tagged_sents)

def q20():
    # text = brown.words()
    # tagged_text = brown.tagged_words()
    # set_text = set(text)
    # cfd = nltk.ConditionalFreqDist(tagged_text)
    # conditions = cfd.conditions()

    # # produces the alphabetically sorted list of distinct words tagged as MD.

    # md_words = [condition for condition in conditions if cfd[condition]['MD'] != 0]
    # md_words.sort()

    # print(md_words)

    # # question two - 2. Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).

    # two_words = [condition for condition in conditions if cfd[condition]['NNS'] and cfd[condition]['VBZ']]
    # two_words.sort()
    # print(two_words)

    # # question four

    # fd = nltk.FreqDist(text)
    # masc_fem_proportion = (fd['he'] + fd['He']) / (fd['she'] + fd['She'])
    # print(masc_fem_proportion)

    # 3. Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).

    # pulls out trigrams for the tagged text
    tagged_text = brown.tagged_words()
    trigrams = list(nltk.trigrams(tagged_text))
    for trigram in trigrams:
        zipped_tag = [t for t in zip(*trigram)]
        if zipped_tag[1] == ('IN', 'DT', 'NN'):
            print(zipped_tag[0])

def q22():
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
    # print.

def q36():
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

if __name__ == '__main__':
    print("\n========= start =========")
    print("\n========= question 10 =========")
    q10()
    print("\n========= finish =========")
