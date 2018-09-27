# p239

fin = open("data/bfile", "rb")
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])
