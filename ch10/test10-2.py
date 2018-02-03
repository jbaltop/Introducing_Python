#!/usr/local/bin/python3

fin = open('today.txt', 'rt')
today_string = fin.read()
fin.close()

print(today_string)
