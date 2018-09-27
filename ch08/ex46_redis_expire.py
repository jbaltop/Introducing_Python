# p282

import redis
import time

conn = redis.Redis()

# clear redis
conn.flushdb()

key = "now you see it"

print(conn.set(key, "but not for long"))
print(conn.expire(key, 5))
print(conn.ttl(key))
print(conn.get(key))

time.sleep(6)
print(conn.get(key))
