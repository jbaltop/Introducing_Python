#!/usr/local/bin/python3

from datetime import datetime

some_day = datetime(2015, 1, 2, 3, 4, 5, 6)
now = datetime.now()

dateAndTimes = [
	some_day,
	some_day.isoformat(),
	now,
	now.year,
	now.month,
	now.day,
	now.hour,
	now.minute,
	now.second,
	now.microsecond
]

for dateAndTime in dateAndTimes:
	print(dateAndTime)
