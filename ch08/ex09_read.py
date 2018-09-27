# p236

poem = ""
fin = open("data/relativity", "rt", encoding="utf-8")
for line in fin:
    poem += line
fin.close()
print(len(poem))
