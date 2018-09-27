# p219

import re

source = """I wish I may, I wish I might
Have a dish of fish tonight."""

m = re.search(r"(. dish\b).*(\bfish)", source)
print(m.group())
print(m.groups())

m = re.search(r"(?P<DISH>. dish\b).*(?P<FISH>\bfish)", source)
print(m.group())
print(m.groups())
print(m.group("DISH"))
print(m.group("FISH"))
