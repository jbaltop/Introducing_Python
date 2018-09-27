# p321

import os

with open("output/oops.txt", "wt", encoding="utf-8") as fout:
    fout.write("")

os.remove("output/oops.txt")
print(os.path.exists("output/oops.txt"))
