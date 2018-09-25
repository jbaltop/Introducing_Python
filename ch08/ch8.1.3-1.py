bdata = bytes(range(0, 256))
print(len(bdata))

fout = open("bfile", "wb")
fout.write(bdata)
fout.close()

fout = open("bfile", "wb")
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset : offset + chunk])
    offset += chunk
fout.close()
