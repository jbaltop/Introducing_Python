# p331

from datetime import date, timedelta

now = date.today()
one_day = timedelta(days=1)

tomorrow = now + one_day
print(tomorrow)
print(now + 17 * one_day)

yesterday = now - one_day
print(yesterday)
