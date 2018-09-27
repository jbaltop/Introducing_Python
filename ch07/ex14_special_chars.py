# p215

import string
import re

printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print("-----")

print(re.findall("\d", printable))
print(re.findall("\w", printable))
print(re.findall("\s", printable))

print("-----")

x = "abc" + "-/*" + "\u00ea" + "\u0115"
print(re.findall("\w", x))
