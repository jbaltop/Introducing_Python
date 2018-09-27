# p248

import json
import datetime
from time import mktime

now = datetime.datetime.utcnow()
print(now)

# json.dumps(now) # TypeError

now_str = str(now)
print(json.dumps(now_str))

now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))
