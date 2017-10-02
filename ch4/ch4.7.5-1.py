#!/usr/local/bin/python3

def print_kwargs(**kwargs):
	print('Keyword arguments:', kwargs)
print(print_kwargs(wine='merlot', entree='mutton', dessert='macaroon'))
