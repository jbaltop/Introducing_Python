# p278

import redis

conn = redis.Redis()

# clear redis
conn.flushdb()

print(conn.sadd("zoo", "duck", "goat", "turkey"))
print(conn.scard("zoo"))
print(conn.smembers("zoo"))
print(conn.srem("zoo", "turkey"))

print("-----")

print(conn.sadd("better_zoo", "tiger", "wolf", "duck"))
print(conn.sinter("zoo", "better_zoo"))
print(conn.sinterstore("fowl_zoo", "zoo", "better_zoo"))
print(conn.smembers("fowl_zoo"))

print("-----")

print(conn.sunion("zoo", "better_zoo"))
print(conn.sunionstore("fabulous_zoo", "zoo", "better_zoo"))
print(conn.smembers("fabulous_zoo"))
print(conn.sdiff("zoo", "better_zoo"))
print(conn.sdiffstore("zoo_sale", "zoo", "better_zoo"))
print(conn.smembers("zoo_sale"))
