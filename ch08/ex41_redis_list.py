# p275

import redis

conn = redis.Redis()

# clear redis
conn.flushdb()

print(conn.lpush("zoo", "bear"))
print(conn.lpush("zoo", "alligator", "duck"))
print(conn.linsert("zoo", "before", "bear", "beaver"))
print(conn.linsert("zoo", "after", "bear", "cassowary"))
print(conn.lset("zoo", 2, "marmoset"))
print(conn.rpush("zoo", "yak"))
print(conn.lindex("zoo", 3))
print(conn.lrange("zoo", 0, 2))
print(conn.ltrim("zoo", 1, 4))
print(conn.lrange("zoo", 0, -1))
