# p319

import os

with open("output/ohno.txt", "wt", encoding="utf-8") as fout:
    fout.write("")
os.remove("output/ohwell.txt")

os.rename("output/ohno.txt", "output/ohwell.txt")
