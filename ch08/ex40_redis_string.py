# p273

import redis

conn = redis.Redis()

# clear redis
conn.flushdb()

print("conn.keys('*')")
print(conn.keys("*"))

print("conn.set('secret', 'ni!')")
print(conn.set("secret", "ni!"))

print("conn.set('carats', '24')")
print(conn.set("carats", "24"))

print("conn.set('fever', '101.5')")
print(conn.set("fever", "101.5"))

print("-----")

print("conn.get('secret')")
print(conn.get("secret"))

print("conn.get('carats')")
print(conn.get("carats"))

print("conn.get('fever')")
print(conn.get("fever"))

print("-----")

print("conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')")
print(conn.setnx("secret", "icky-icky-icky-ptang-zoop-boing!"))

print("conn.get('secret')")
print(conn.get("secret"))

print("conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')")
print(conn.getset("secret", "icky-icky-icky-ptang-zoop-boing!"))

print("conn.get('secret')")
print(conn.get("secret"))

print("conn.getrange('secret', -6, -1)")
print(conn.getrange("secret", -6, -1))

print("conn.setrange('secret', 0, 'ICKY')")
print(conn.setrange("secret", 0, "ICKY"))

print("conn.get('secret')")
print(conn.get("secret"))

print("-----")

print("conn.mset({'pie': 'cherry', 'cordial': 'sherry'})")
print(conn.mset({"pie": "cherry", "cordial": "sherry"}))

print("conn.mget(['fever', 'carats'])")
print(conn.mget(["fever", "carats"]))

print("-----")

print("conn.incr('carats')")
print(conn.incr("carats"))

print("conn.incr('carats', 10)")
print(conn.incr("carats", 10))

print("conn.decr('carats')")
print(conn.decr("carats"))

print("conn.decr('carats', 15)")
print(conn.decr("carats", 15))

print("conn.incrbyfloat('fever')")
print(conn.incrbyfloat("fever"))

print("conn.incrbyfloat('fever', 0.5)")
print(conn.incrbyfloat("fever", 0.5))

print("conn.incrbyfloat('fever', -2.0)")
print(conn.incrbyfloat("fever", -2.0))

print("-----")

print("conn.delete('fever')")
print(conn.delete("fever"))
