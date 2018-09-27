# p100

drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua"},
    "white russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"},
}
for name, contents in drinks.items():
    if contents & {"vermouth", "orange juice"}:
        print(name)

print("-----")

for name, contents in drinks.items():
    if "vodka" in contents and not contents & {"vermouth", "cream"}:
        print(name)

bruss = drinks["black russian"]
wruss = drinks["white russian"]

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))
print(bruss & wruss)

print(a | b)
print(a.union(b))
print(bruss | wruss)

print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)

print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)
