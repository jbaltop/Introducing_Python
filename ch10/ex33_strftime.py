# p336

from datetime import date, time

some_day = date(2015, 12, 12)
some_time = time(10, 35)
fmt = "It's %B %d, %Y, local time %I:%M:%S%p"

print(some_day.strftime(fmt))
print(some_time.strftime(fmt))
