#!/usr/local/bin/python3

from datetime import date, timedelta

birthday = date(1999, 9, 3)
d = birthday + timedelta(days=10000)

print(d)
