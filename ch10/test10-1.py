#!/usr/local/bin/python3

from datetime import date

fout = open('today.txt', 'wt')
print(date.today(), file=fout)
fout.close()
