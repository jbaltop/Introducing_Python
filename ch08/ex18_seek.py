# p240

fin = open("data/bfile", "rb")
print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])
