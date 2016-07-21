import pymongo

def main():
    db = pymongo.MongoClient()
    pipeline = [{                                              
        '$group': { 
          '_id':   { 'hour': '$hour', 'city': '$city' }, 
          'count': { '$sum': '$count' } 
        } 
      }]
    for r in db.cities.command('aggregate', 'minute', pipeline=pipeline)['result']:
        print '%s,%s,%s' % (r['_id']['city'], r['_id']['hour'], r['count'])

if __name__ == '__main__':
    main()