# p85

a = [1, 2, 3]
print(a)

b = a
print(b)

a[0] = "surprise"
print(a)
print(b)

b[0] = "I hate surprise"
print(b)
print(a)

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = "integer lists are boring"
print(a)
print(b)
print(c)
print(d)
