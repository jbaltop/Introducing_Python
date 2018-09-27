# p199

import unicodedata

place = "café"
print(place)
print(unicodedata.name("\u00e9"))
print(unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE"))

place = "caf\u00e9"
print(place)

u_umlaut = "\N{LATIN SMALL LETTER U WITH DIAERESIS}"
print(u_umlaut)

drink = "Gew" + u_umlaut + "rztraminer"
print("Now I can finally have my", drink, "in a", place)

print(len("$"))
print(len("\U0001f47b"))
