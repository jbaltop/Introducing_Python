fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

import os

print(os.SEEK_SET)
os.SEEK_CUR
print(os.SEEK_END)

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])
