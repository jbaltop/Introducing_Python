#!/usr/local/bin/python3

animal = 'fruitbat'
def change_local():
	animal = 'wonbat'
	print('locals:', locals())
print(animal)
change_local()
print('globals:', globals())
print(animal)
