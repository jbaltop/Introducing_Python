#!/usr/local/bin/python3

cheeses = []
for cheese in cheeses:
	print('This shop has some lovely', cheese)
	break
else: # break 문이 호출되지 않았다면 cheeses가 없는 것이다.
	print('This is nit much of a cheese shop, is it?')
