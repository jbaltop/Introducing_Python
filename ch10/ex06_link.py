# p320

# not available for windows

import os

with open("output/oops.txt", "wt", encoding="utf-8") as fout:
    fout.write("")

os.link("output/oops.txt", "output/yikes.txt")
print(os.path.isfile("output/yikes.txt"))

print(os.path.islink("output/yikes.txt"))
os.symlink("output/oops.txt", "output/jeepers.txt")
print(os.path.islink("output/jeepers.txt"))
