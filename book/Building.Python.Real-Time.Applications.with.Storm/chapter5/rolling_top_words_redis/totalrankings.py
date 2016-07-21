import logging
import math
import time

import redis

from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('totalrankings')

class TotalRankingsBolt(BasicBolt):
    emitFrequencyInSeconds = 15
    maxSize = 10

    def __init__(self):
        super(TotalRankingsBolt, self).__init__(script=__file__)
        self.rankedItems = {}

    def initialize(self, conf, context):
        self.conf = conf
        self.num_windows = self.conf['twitter_word_count.num_windows']
        self.window_duration = self.conf['twitter_word_count.window_duration']
        self.conn = redis.from_url(conf['twitter_word_count.redis_url'])

    def declareOutputFields(self):
        return ['word', 'count']

    def process(self, tup):
        if tup.is_tick_tuple():
            now = time.time()
            now_floor = int(math.floor(now / self.window_duration) * self.window_duration)
            first_window = int(now_floor - self.num_windows * self.window_duration)
            self.conn.zunionstore(
                'twitter_word_count',
                ['twitter_word_count:%s' % t for t in xrange(first_window, now_floor)])
            for t in self.conn.zrevrange('twitter_word_count', 0, self.maxSize, withscores=True):
                log.info('Emitting: %s', repr(t))
                storm.emit(t)

    def getComponentConfiguration(self):
        return {"topology.tick.tuple.freq.secs": self.emitFrequencyInSeconds}

def run():
    TotalRankingsBolt().run()
