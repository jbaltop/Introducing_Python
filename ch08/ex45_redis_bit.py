# p281

import redis

conn = redis.Redis()

# clear redis
conn.flushdb()

days = ["2013-02-25", "2013-02-26", "2013-02-27"]
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

print(conn.setbit(days[0], big_spender, 1))
print(conn.setbit(days[0], tire_kicker, 1))
print(conn.setbit(days[1], big_spender, 1))
print(conn.setbit(days[2], big_spender, 1))
print(conn.setbit(days[2], late_joiner, 1))

print("-----")

for day in days:
    print(conn.bitcount(day))

print("-----")

print(conn.getbit(days[1], tire_kicker))
print(conn.bitop("and", "everyday", *days))
print(conn.bitcount("everyday"))
print(conn.getbit("everyday", big_spender))
print(conn.bitop("or", "alldays", *days))
print(conn.bitcount("alldays"))
