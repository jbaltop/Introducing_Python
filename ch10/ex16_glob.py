# p324

import glob
import os

os.chdir("output/poems")
print(glob.glob("m*"))
print(glob.glob("??"))
print(glob.glob("m??????e"))
print(glob.glob("[klm]*e"))
