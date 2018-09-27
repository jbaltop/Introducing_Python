# p285

import redis

conn = redis.Redis()

conn.hmset("test", {"count": 1, "name": "Fester Bestertester"})
conn.hincrby("test", "count", 3)

print(conn.hget("test", "count"))
