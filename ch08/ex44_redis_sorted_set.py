# p280

import redis
import time

conn = redis.Redis()

# clear redis
conn.flushdb()

now = time.time()
print(now)

print(conn.zadd("logins", "smeagol", now))
print(conn.zadd("logins", "sauron", now + (5 * 60)))
print(conn.zadd("logins", "bilbo", now + (2 * 60 * 60)))
print(conn.zadd("logins", "treeebeard", now + (24 * 60 * 60)))

print("-----")

print(conn.zrank("logins", "bilbo"))
print(conn.zscore("logins", "bilbo"))
print(conn.zrange("logins", 0, -1))
print(conn.zrange("logins", 0, -1, withscores=True))
