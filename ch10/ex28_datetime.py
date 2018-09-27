# p333

from datetime import datetime, time, date

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)

print(noon_today)
print(noon_today.date())
print(noon_today.time())
