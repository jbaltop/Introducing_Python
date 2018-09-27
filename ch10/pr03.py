# p339

import time

with open("data/today.txt", "rt", encoding="utf-8") as fin:
    today_string = fin.read()

fmt = "%Y-%m-%d\n"
print(time.strptime(today_string, fmt))
