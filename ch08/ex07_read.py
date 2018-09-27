# p235

poem = ""
fin = open("data/relativity", "rt", encoding="utf-8")
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))
