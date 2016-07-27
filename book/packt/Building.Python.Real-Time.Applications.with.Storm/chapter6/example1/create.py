from randomsentence import RandomSentenceSpout
from splitsentence import SplitSentenceBolt
from wordcount import WordCountBolt

def create(builder):
    builder.setSpout("spout", RandomSentenceSpout(), 1)
    builder.setBolt(
        "split", SplitSentenceBolt(), 1).shuffleGrouping("spout")
    builder.setBolt(
        "count", WordCountBolt(), 1).fieldsGrouping("split", ["word"])
