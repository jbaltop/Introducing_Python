# p237

bdata = bytes(range(0, 256))
print(len(bdata))

fout = open("output/bfile", "wb")
fout.write(bdata)
fout.close()
