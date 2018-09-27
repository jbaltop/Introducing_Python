# p242

import csv

with open("data/villains", "rt", encoding="utf-8") as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)
