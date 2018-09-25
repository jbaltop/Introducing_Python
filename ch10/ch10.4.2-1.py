import time

now = time.time()

dateAndTimes = [
	now,
	time.ctime(now)
]

for dateAndTime in dateAndTimes:
	print(dateAndTime)
