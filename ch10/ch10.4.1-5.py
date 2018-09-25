from datetime import datetime, time, date

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)

dateAndTimes = [noon_today, noon_today.date(), noon_today.time()]

for dateAndTime in dateAndTimes:
    print(dateAndTime)
