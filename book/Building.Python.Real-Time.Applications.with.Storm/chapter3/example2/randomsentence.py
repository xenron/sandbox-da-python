import time
import random

from petrel import storm
from petrel.emitter import Spout

class RandomSentenceSpout(Spout):
    def __init__(self):
        super(RandomSentenceSpout, self).__init__(script=__file__)

    @classmethod
    def declareOutputFields(cls):
        return ['sentence']

    sentences = [
        "the cow jumped over the moon",
        "an apple a day keeps the doctor away",
    ]
        
    def nextTuple(self):
        time.sleep(0.25)
        sentence = self.sentences[random.randint(0, len(self.sentences) - 1)]
        storm.emit([sentence])

def run():
    RandomSentenceSpout().run()
