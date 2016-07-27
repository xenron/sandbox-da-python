import logging

from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('totalrankings')

def tup_sort_key(tup):
    return tup.values[1]


class TotalRankingsBolt(BasicBolt):
    emitFrequencyInSeconds = 15
    maxSize = 10

    def __init__(self):
        super(TotalRankingsBolt, self).__init__(script=__file__)
        self.rankedItems = {}

    def declareOutputFields(self):
        return ['word', 'count']

    def process(self, tup):
        if tup.is_tick_tuple():
            for t in sorted(
                    self.rankedItems.itervalues(),
                    key=tup_sort_key,
                    reverse=True):
                log.info('Emitting: %s', repr(t.values))
                storm.emit(t.values)
        else:
            self.rankedItems[tup.values[0]] = tup
            if len(self.rankedItems) > self.maxSize:
                for t in sorted(
                        self.rankedItems.itervalues(),
                        key=tup_sort_key):
                    del self.rankedItems[t.values[0]]
                    break
            zero_keys = set(
                k for k, v in self.rankedItems.iteritems()
                if v.values[1] == 0)
            for k in zero_keys:
                del self.rankedItems[k]

    def getComponentConfiguration(self):
        return {"topology.tick.tuple.freq.secs": self.emitFrequencyInSeconds}

def run():
    TotalRankingsBolt().run()
