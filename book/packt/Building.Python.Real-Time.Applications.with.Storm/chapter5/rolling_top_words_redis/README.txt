Install Redis server on one well-known node. All workers will store state here.

sudo apt-get install redis-server

Install Python Redis client on all Storm worker machines:

sudo apt-get install python-redis

Run the topology:

petrel submit --config topology.yaml --logdir `pwd`

Example output from totalrankings:
[2015-08-10 21:30:01,691][totalrankings][INFO]Emitting: ('love', 74.0)
[2015-08-10 21:30:01,691][totalrankings][INFO]Emitting: ('amp', 68.0)
[2015-08-10 21:30:01,691][totalrankings][INFO]Emitting: ('like', 67.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('zaynmalik', 61.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('mtvhottest', 61.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('get', 58.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('one', 49.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('follow', 46.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('u', 44.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('new', 38.0)
[2015-08-10 21:30:01,692][totalrankings][INFO]Emitting: ('much', 37.0)
