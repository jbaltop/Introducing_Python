# p320

import os

try:
    with open("output/oops2.txt", "wt", encoding="utf-8") as fout:
        fout.write("")
except:
    os.chmod("output/oops2.txt", 0o777)

os.chmod("output/oops2.txt", 0o400)

import stat

os.chmod("output/oops2.txt", stat.S_IRUSR)
