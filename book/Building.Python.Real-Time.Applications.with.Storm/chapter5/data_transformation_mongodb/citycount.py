import datetime
import logging

import geotext
import nltk.corpus
import pymongo

from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('citycount')

class CityCountBolt(BasicBolt):
    def __init__(self):
        super(CityCountBolt, self).__init__(script=__file__)
        self.stop_words = set(nltk.corpus.stopwords.words('english'))
        self.stop_words.update(['http', 'https', 'rt'])
        self.stop_cities = set([
            'bay', 'best', 'deal', 'man', 'metro', 'of', 'un'])

    def initialize(self, conf, context):
        self.db = pymongo.MongoClient()

    def declareOutputFields(self):
        return []

    def process(self, tup):
        clean_text = ' '.join(w for w in self._get_words(tup.values[0]))
        places = geotext.GeoText(clean_text)
        now_minute = self._get_minute()
        now_hour = now_minute.replace(minute=0)
        for city in places.cities:
            city = city.lower()
            if city in self.stop_cities:
                continue
            log.info('Updating count: %s, %s, %s', now_hour, now_minute, city)
            self.db.cities.minute.update(
                {
                    'hour': now_hour,
                    'minute': now_minute,
                    'city': city
                },
                {'$inc': { 'count' : 1 } },
                upsert=True)

    @staticmethod
    def _get_minute():
            return datetime.datetime.now().replace(second=0, microsecond=0)

    def _get_words(self, sentence):
        for w in nltk.word_tokenize(sentence):
            wl = w.lower()
            if wl.isalpha() and wl not in self.stop_words:
                yield w
            
def run():
    CityCountBolt().run()
