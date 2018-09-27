# p241

import csv

villains = [
    ["Doctor", "No"],
    ["Rosa", "Klebb"],
    ["Mister", "Big"],
    ["Auric", "Goldfinger"],
    ["Ernst", "Blofeld"],
]

with open("output/villains", "wt", encoding="utf-8", newline="") as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
