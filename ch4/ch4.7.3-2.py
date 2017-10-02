#!/usr/local/bin/python3

def buggy(arg, result=[]):
	result.append(arg)
	print(result)
print(buggy('a'))
print(buggy('b'))
