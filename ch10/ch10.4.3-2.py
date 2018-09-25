import time

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()

dateAndTimes = [t, time.strftime(fmt, t)]

for dateAndTime in dateAndTimes:
    print(dateAndTime)
