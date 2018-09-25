import memcache

db = memcache.Client(['127.0.0.1:11211'])
print(db.set('marco', 'polo'))
print(db.get('marco'))
print(db.set('ducks', 0))
print(db.get('ducks'))
print(db.incr('ducks', 2))
print(db.get('ducks'))
