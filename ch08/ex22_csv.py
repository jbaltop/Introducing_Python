# p243

import csv

villains = [
    {"first": "Doctor", "last": "No"},
    {"first": "Rosa", "last": "Big"},
    {"first": "Mister", "last": "Big"},
    {"first": "Auric", "last": "Goldfinger"},
    {"first": "Ernst", "last": "Blofeld"},
]

with open("output/villains", "wt", encoding="utf-8", newline="") as fout:
    cout = csv.DictWriter(fout, ["first", "last"])
    cout.writeheader()
    cout.writerows(villains)
