# p235

poem = ""
fin = open("data/relativity", "rt", encoding="utf-8")
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))
