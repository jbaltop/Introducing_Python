import string
import re

printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall("\d", printable))
print(re.findall("\w", printable))
print(re.findall("\s", printable))

x = "abc" + "-/*" + "\u00ea" + "\u0115"
print(re.findall("\w", x))

source = """I wish I may, I wish I might
Have a dish of fish tonight."""
print(re.findall("wish", source))
print(re.findall("wish|fish", source))
print(re.findall("^wish", source))
print(re.findall("^I wish", source))
print(re.findall("fish$", source))
print(re.findall("fish tonight.$", source))
print(re.findall("fish tonight\.$", source))
print(re.findall("[wf]ish", source))
print(re.findall("[wsh]+", source))
print(re.findall("ght\W", source))
print(re.findall("I (?=wish)", source))
print(re.findall("(?<=I) wish", source))
print(re.findall(r"\bfish", source))

m = re.search(r"(. dish\b).*(\bfish)", source)
print(m.group())
print(m.groups())

m = re.search(r"(?P<DISH>. dish\b).*(?P<FISH>\bfish)", source)
print(m.group())
print(m.groups())
print(m.group("DISH"))
print(m.group("FISH"))
