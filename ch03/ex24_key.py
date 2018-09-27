# p91

pythons = {
    "Chapman": "Graham",
    "Cleese": "John",
    "Idle": "Eric",
    "Jones": "Terry",
    "Palin": "Michael",
}
print(pythons)

pythons["Gilliam"] = "Gerry"
print(pythons)

pythons["Gilliam"] = "Terry"
print(pythons)

some_pythons = {
    "Graham": "Chapman",
    "John": "Cleese",
    "Eric": "Idle",
    "Terry": "Gilliam",
    "Michael": "Palin",
    "Terry": "Jones",
}
print(some_pythons)
