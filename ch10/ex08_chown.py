# p321

# not available for windows

import os

with open("output/oops", "wt", encoding="utf-8") as fout:
    fout.write("")

uid = 5
gid = 22

os.chown("output/oops", uid, gid)
