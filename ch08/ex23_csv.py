# p243

import csv

with open("data/villains", "rt", encoding="utf-8") as fin:
    cin = csv.DictReader(fin, fieldnames=["first", "last"])
    villains = [row for row in cin]
print(villains)
