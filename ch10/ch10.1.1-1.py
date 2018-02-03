#!/usr/local/bin/python3

fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()
