# p213


import re

source = "Young Frankenstein"

m = re.search("Frank", source)
if m:
    print(m.group())
