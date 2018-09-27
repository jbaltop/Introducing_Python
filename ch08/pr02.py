# p284

test1 = "This is a test of the emergency text system"

with open("output/test.txt", "wt", encoding="utf-8") as fout:
    fout.write(test1)

with open("output/test.txt", "rt", encoding="utf-8") as fin:
    test2 = fin.read()

print(test1 == test2)
