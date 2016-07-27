import logging
from collections import defaultdict

from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('wordcount')

class WordCountBolt(BasicBolt):
    def __init__(self):
        super(WordCountBolt, self).__init__(script=__file__)
        self._count = defaultdict(int)

    @classmethod
    def declareOutputFields(cls):
        return ['word', 'count']

    def process(self, tup):
        raise ValueError('abc')
        log.debug('WordCountBolt.process() called with: %s', tup)
        word = tup.values[0]
        self._count[word] += 1
        log.debug('WordCountBolt.process() emitting: %s', [word, self._count[word]])
        storm.emit([word, self._count[word]])

def run():
    WordCountBolt().run()
