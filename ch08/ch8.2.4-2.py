import json
import datetime

now = datetime.datetime.utcnow()
print(now)

now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

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
print(type('hey'))
print(isinstance('hey', str))
