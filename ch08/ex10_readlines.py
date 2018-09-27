# p236

fin = open("data/relativity", "rt", encoding="utf-8")
lines = fin.readlines()
fin.close()
print(len(lines), "lines read")
for line in lines:
    print(line, end="")
