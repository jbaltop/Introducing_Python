import time

now = time.time()
tm = time.localtime(now)

dateAndTimes = [
	time.localtime(now),
	time.gmtime(now),
	time.mktime(tm)
]

for dateAndTime in dateAndTimes:
	print(dateAndTime)
