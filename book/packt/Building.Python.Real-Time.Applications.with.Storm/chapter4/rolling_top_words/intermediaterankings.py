from petrel import storm
from petrel.emitter import BasicBolt

def tup_sort_key(tup):
    return tup.values[1]


class IntermediateRankingsBolt(BasicBolt):
    emitFrequencyInSeconds = 15
    maxSize = 10

    def __init__(self):
        super(IntermediateRankingsBolt, self).__init__(script=__file__)
        self.rankedItems = {}

    def declareOutputFields(self):
        return ['word', 'count']

    def process(self, tup):
        if tup.is_tick_tuple():
            for t in self.rankedItems.itervalues():
                storm.emit(t.values)
        else:
            self.rankedItems[tup.values[0]] = tup
            if len(self.rankedItems) > self.maxSize:
                for t in sorted(
                        self.rankedItems.itervalues(), key=tup_sort_key):
                    del self.rankedItems[t.values[0]]
                    break

    def getComponentConfiguration(self):
        return {"topology.tick.tuple.freq.secs":
            self.emitFrequencyInSeconds}

def run():
    IntermediateRankingsBolt().run()
