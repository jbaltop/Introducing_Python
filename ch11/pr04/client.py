# p392

import redis
from datetime import datetime as dt
from time import sleep

conn = redis.Redis()
timeout = 10
conveyor = "chocolates"
while True:
    sleep(0.5)
    msg = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if msg:
        piece = msg[1]
        print("Lucy got a", piece, "at", dt.utcnow(), ", only", remaining, "left")
