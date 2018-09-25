#!/usr/local/bin/python3

import redis

conn = redis.Redis()
print(conn.lpush('zoo', 'bear'))
print(conn.lpush('zoo', 'alligator', 'duck'))
print(conn.lpush('zoo', 'before', 'bear', 'beaver'))
print(conn.lpush('zoo', 'after', 'bear', 'cassowary'))
print(conn.lpush('zoo', 2, 'marmoset'))
print(conn.rpush('zoo', 'yak'))
print(conn.lindex('zoo', 3))
print(conn.lrange('zoo', 0, 2))
print(conn.ltrim('zoo', 1, 4))
print(lrange('zoo', 0, -1))
