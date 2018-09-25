#!/usr/local/bin/python3

def knights(saying):
	def inner(quote):
		return "We are the knights who say: '%s'" % quote
	return inner(saying)
print(knights('Ni!'))
