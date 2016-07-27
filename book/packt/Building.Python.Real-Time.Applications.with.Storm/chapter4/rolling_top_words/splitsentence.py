import nltk.corpus

from petrel import storm
from petrel.emitter import BasicBolt

class SplitSentenceBolt(BasicBolt):
    def __init__(self):
        super(SplitSentenceBolt, self).__init__(script=__file__)
        self.stop = set(nltk.corpus.stopwords.words('english'))
        self.stop.update(['http', 'https', 'rt'])

    def declareOutputFields(self):
        return ['word']

    def process(self, tup):
        for word in self._get_words(tup.values[0]):
            storm.emit([word])

    def _get_words(self, sentence):
        for w in nltk.word_tokenize(sentence):
            w = w.lower()
            if w.isalpha() and w not in self.stop:
                yield w

def run():
    SplitSentenceBolt().run()
