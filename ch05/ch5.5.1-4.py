#!/usr/local/bin/python3

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
	if not food in dict_counter:
		dict_counter[food] = 0
	dict_counter[food] += 1
for food, count in dict_counter.items():
	print(food, count)
