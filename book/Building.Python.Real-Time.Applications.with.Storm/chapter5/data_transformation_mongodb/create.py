from twitterstream import TwitterStreamSpout
from citycount import CityCountBolt

def create(builder):
    spoutId = "spout"
    cityCountId = "citycount"
    builder.setSpout(spoutId, TwitterStreamSpout(), 1)
    builder.setBolt(
        cityCountId, CityCountBolt(), 1).shuffleGrouping("spout")
