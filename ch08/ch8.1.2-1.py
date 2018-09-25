#!/usr/local/bin/python3

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
chunk = 50
while True:
	fragment = fin.read(chunk)
	if not fragment:
		break
	poem += fragment
fin.close()
print(len(poem))
