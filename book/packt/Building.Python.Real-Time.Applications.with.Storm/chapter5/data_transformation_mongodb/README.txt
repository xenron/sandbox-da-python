This is a variant of the Twitter sample which:
1. Uses the Python geotext library (https://pypi.python.org/pypi/geotext) to find city names in Tweets
2. Stores a per-minute time series of city counts in MongoDB.
3. Includes a standalone script which computes hourly counts by city.

twitterstream.py has not changed. The modified files are:
* create.py: Creates the topology
* citycount.py: Bolt that finds city names and writes to MongoDB. It is similar to the SplitSentenceBolt from the Twitter sample, but after splitting by words, it looks for city names and skips some common words that often appear in tweets that geotext identifies as city names but probably aren't. The _get_words() function changes slightly because geotext won't recognize lower-case strings as city names. It creates or updates MongoDB records, taking advantage of the unique index on minute and city to build per-minute counts. This is a typical way to represent time series in MongoDB. Each record also includes an "hour" field, which is used by the city_report.py script.
* city_report.py: Standalone hourly report script. Uses MongoDB aggregation to compute the hourly totals. Note the report depends on the presence of an "hour" field. Due to the limited capabilities of aggregation expressions in MongoDB, this is the simplest way to aggregate by hour.
* setup.sh

==

Install MongoDB server. On Ubuntu, you can use these instructions:
http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

Install Python MongoDB client on all Storm worker machines:
pip install pymongo==3.0.3

Install geotext:
pip install geotext==0.1.0

==

This example uses a MongoDB database called cities, with a collection named "minute".

In order to compute the counts by city and minute, we must create a unique index on the cities.minute collection. To do this, launch the MongoDB command-line client:

mongo

Create a unique index on the cities.minute collection:

use cities
db.minute.createIndex( { minute: 1, city: 1 }, { unique: true } )

==

To verify pymongo is installed and the index was created correctly, start an interactive Python session by running "python". Then:

import pymongo
from pymongo import MongoClient
db = MongoClient()
for index in db.cities.minute.list_indexes(): print index

You should see the following. The second line is the index we added.
SON([(u'v', 1), (u'key', SON([(u'_id', 1)])), (u'name', u'_id_'), (u'ns', u'cities.minute')])
SON([(u'v', 1), (u'unique', True), (u'key', SON([(u'minute', 1.0), (u'city', 1.0)])), (u'name', u'minute_1_city_1'), (u'ns', u'cities.minute')])

==

Run the topology:

petrel submit --config topology.yaml --logdir `pwd`

==

References:

Storing in MongoDB:
http://stats.seandolinar.com/collecting-twitter-data-storing-tweets-in-mongodb/

Indexing by date:
http://docs.mongodb.org/manual/core/index-compound/
