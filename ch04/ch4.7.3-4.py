#!/usr/local/bin/python3

def nonbuggy(arg, result=None):
	if result is None:
		result = []
	result.append(arg)
	print(result)
print(nonbuggy('a'))
print(nonbuggy('b'))
