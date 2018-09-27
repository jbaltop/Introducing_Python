# p248

import json
import datetime
from time import mktime

now = datetime.datetime.utcnow()


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)


print(json.dumps(now, cls=DTEncoder))

print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type("hey"))
print(isinstance("hey", str))
