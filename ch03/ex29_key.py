# p94

pythons = {
    "Chapman": "Graham",
    "Cleese": "John",
    "Gilliam": "Terry",
    "Idle": "Eric",
    "Jones": "Terry",
    "Palin": "Michael",
}
print(pythons["Cleese"])
# print(pythons['Marx']) # KeyError

print(pythons.get("Cleese"))
print(pythons.get("Marx", "Not a Python"))
print(pythons.get("Marx"))
