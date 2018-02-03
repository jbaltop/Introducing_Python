#!/usr/local/bin/python3

from datetime import time

noon = time(12, 0, 0)

times = [noon, noon.hour, noon.minute, noon.second, noon.microsecond]

for time in times:
	print(time)
