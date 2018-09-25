#!/usr/local/bin/python3

import csv

villains = [
	['Doctor', 'No'],
	['Rosa', 'Klebb'],
	['Mister', 'Big'],
	['Auric', 'Goldfinger'],
	['Ernst', 'Blofeld'],
	]

with open('villains', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(villains)

with open('villains', 'rt') as fin:
	cin = csv.reader(fin)
	villains = [row for row in cin]
print(villains)
