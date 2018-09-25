#!/usr/local/bin/python3

class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
