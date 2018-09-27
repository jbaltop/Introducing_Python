# p336

import time

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))
