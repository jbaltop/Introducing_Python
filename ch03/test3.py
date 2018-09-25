year_lists = ["1980", "1981", "1982", "1983", "1984", "1985"]
print(year_lists[3])
print(year_lists[-1])
things = ["mozzarella", "cinderella", "salmonella"]
print(things[1].capitalize())
print(things[0].upper())
del things[2]
print(things)
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1].lower()
print(surprise[-1][::-1].capitalize())
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)
print(e2f["walrus"])
a, b, c = e2f.items()
e, f = a
A = {}
A[f] = e
e, f = b
B = {}
B[f] = e
e, f = c
C = {}
C[f] = e
f2e = A
f2e.update(B)
f2e.update(C)
print(f2e)
print(f2e["chien"])
print(e2f.keys())
life = {
    "animals": {"cats": ["Henry", "Grumpy", "Lucy"], "octopi": {}, "emus": {}},
    "plants": {},
    "others": {},
}
print(life.keys())
print(life["animals"].keys())
print(life["animals"]["cats"])
