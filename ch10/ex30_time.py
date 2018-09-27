# p334

import time

now = time.time()
print(time.localtime(now))
print(time.gmtime(now))

tm = time.localtime(now)
print(time.mktime(tm))
