import redis

conn = redis.Redis()
print(conn.hmset("song", {"do": "a deer", "re": "about a deer"}))
print(conn.hset("song", "mi", "a note to follow re"))
print(conn.hget("song", "mi"))
print(conn.hmget("song", "re", "do"))
print(hkeys("song"))
print(conn.hvals("song"))
print(conn.hlen("song"))
print(conn.hgetall("song"))
print(conn.hsetnx("song", "fa", "a note that rhymes with la"))
