#!/usr/local/bin/python3

from datetime import date, timedelta

now = date.today()
one_day = timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day

days = [
	now,
	tomorrow,
	now + 17*one_day,
	yesterday
]

for day in days:
	print(day)
