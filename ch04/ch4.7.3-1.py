#!/usr/local/bin/python3

def menu(wine, entree, dessert='pudding'):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))
