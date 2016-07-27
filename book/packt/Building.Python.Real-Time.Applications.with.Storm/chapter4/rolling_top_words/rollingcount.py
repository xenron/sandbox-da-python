from collections import defaultdict

from petrel import storm
from petrel.emitter import BasicBolt

class SlotBasedCounter(object):
    def __init__(self, numSlots):
        self.numSlots = numSlots
        self.objToCounts = defaultdict(lambda: [0] * numSlots)

    def incrementCount(self, obj, slot):
        self.objToCounts[obj][slot] += 1

    def getCount(self, obj, slot):
        return self.objToCounts[obj][slot]

    def getCounts(self):
        return dict((k, sum(v)) for k, v in self.objToCounts.iteritems())

    def wipeSlot(self, slot):
        for obj in self.objToCounts.iterkeys():
            self.objToCounts[obj][slot] = 0

    def shouldBeRemovedFromCounter(self, obj):
        return sum(self.objToCounts[obj]) == 0

    def wipeZeros(self):
        objToBeRemoved = set()
        for obj in self.objToCounts.iterkeys():
            if sum(self.objToCounts[obj]) == 0:
                objToBeRemoved.add(obj)
        for obj in objToBeRemoved:
            del self.objToCounts[obj]


class SlidingWindowCounter(object):
    def __init__(self, windowLengthInSlots):
        self.windowLengthInSlots = windowLengthInSlots
        self.objCounter = SlotBasedCounter(self.windowLengthInSlots)
        self.headSlot = 0
        self.tailSlot = self.slotAfter(self.headSlot)

    def incrementCount(self, obj):
        self.objCounter.incrementCount(obj, self.headSlot)

    def getCountsThenAdvanceWindow(self):
        counts = self.objCounter.getCounts()
        self.objCounter.wipeZeros()
        self.objCounter.wipeSlot(self.tailSlot)
        self.headSlot = self.tailSlot
        self.tailSlot = self.slotAfter(self.tailSlot)
        return counts

    def slotAfter(self, slot):
        return (slot + 1) % self.windowLengthInSlots


class RollingCountBolt(BasicBolt):
    numWindowChunks = 5
    emitFrequencyInSeconds = 60
    windowLengthInSeconds = numWindowChunks * emitFrequencyInSeconds

    def __init__(self):
        super(RollingCountBolt, self).__init__(script=__file__)
        self.counter = SlidingWindowCounter(
            self.windowLengthInSeconds / self.emitFrequencyInSeconds)

    @classmethod
    def declareOutputFields(cls):
        return ['word', 'count']

    def process(self, tup):
        if tup.is_tick_tuple():
            self.emitCurrentWindowCounts()
        else:
            self.counter.incrementCount(tup.values[0])

    def emitCurrentWindowCounts(self):
        counts = self.counter.getCountsThenAdvanceWindow()
        for k, v in counts.iteritems():
            storm.emit([k, v])

    def getComponentConfiguration(self):
        return {"topology.tick.tuple.freq.secs":
            self.emitFrequencyInSeconds}


def run():
    RollingCountBolt().run()
