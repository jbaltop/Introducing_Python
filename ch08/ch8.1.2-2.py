poem = ""
fin = open("relativity", "rt")
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

poem = ""
fin = open("relativity", "rt")
for line in fin:
    poem += line
fin.close()
print(len(poem))

fin = open("relativity", "rt")
lines = fin.readlines()
fin.close()
print(len(lines), "lines read")
for line in lines:
    print(line, end="")
