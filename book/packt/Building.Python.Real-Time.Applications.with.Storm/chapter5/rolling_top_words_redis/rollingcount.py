import logging
import math
import time

from collections import defaultdict

import redis

from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('rollingcount')

class RollingCountBolt(BasicBolt):
    def __init__(self):
        super(RollingCountBolt, self).__init__(script=__file__)

    def initialize(self, conf, context):
        self.conf = conf
        self.num_windows = self.conf['twitter_word_count.num_windows']
        self.window_duration = self.conf['twitter_word_count.window_duration']
        self.conn = redis.from_url(conf['twitter_word_count.redis_url'])

    @classmethod
    def declareOutputFields(cls):
        return ['word', 'count']

    def process(self, tup):
        word = tup.values[0]
        now = time.time()
        now_floor = int(math.floor(now / self.window_duration) * self.window_duration)
        expires = int(now_floor + self.num_windows * self.window_duration)
        name = 'twitter_word_count:%s' % now_floor
        self.conn.zincrby(name, word)
        self.conn.expireat(name, expires)


def run():
    RollingCountBolt().run()
