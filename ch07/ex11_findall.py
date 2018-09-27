# p213

import re

source = "Young Frankenstein"

m = re.findall("n", source)
print(m)
print("Found", len(m), "matches")

m = re.findall("n.", source)
print(m)

m = re.findall("n.?", source)
print(m)
