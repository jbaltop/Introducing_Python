# p238

fin = open("data/bfile", "rb")
print(fin.tell())
print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])
