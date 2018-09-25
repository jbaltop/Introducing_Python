class OopsException(Exception):
	pass
raise OopsException()
try:
	raise OopsException
except OopsException:
	print('Caught an oops')
