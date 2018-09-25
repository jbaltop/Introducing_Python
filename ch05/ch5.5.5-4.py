import itertools
def multiply(a, b):
	return a * b
for item in itertools.accumulate([1, 2, 3, 4], multiply):
	print(item)
