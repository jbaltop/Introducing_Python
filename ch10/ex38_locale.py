# p338

import locale

names = locale.locale_alias.keys()
good_names = [name for name in names if len(name) == 5 and name[2] == "_"]

print(good_names[:5])

de = [name for name in good_names if name.startswith("de")]

print(de)
