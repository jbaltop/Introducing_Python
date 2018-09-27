# p102

bruss = {"vodka", "kahlua"}
wruss = {"cream", "kahlua", "vodka"}
a = {1, 2}
b = {2, 3}

print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)
print(a.issubset(a))

print("-----")

print(a < b)
print(a < a)
print(bruss < wruss)

print("-----")

print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
print(a >= a)
print(a.issuperset(a))

print("-----")

print(a > b)
print(wruss > bruss)
print(a > a)
