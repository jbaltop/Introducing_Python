import csv

with open("villains", "rt") as fin:
    cin = csv.DictReader(fin, fieldnames=["first", "last"])
    villains = [row for row in cin]
print(villains)

villains = [
    {"first": "Doctor", "last": "No"},
    {"first": "Rosa", "last": "Big"},
    {"first": "Mister", "last": "Big"},
    {"first": "Auric", "last": "Goldfinger"},
    {"first": "Ernst", "last": "Blofeld"},
]
with open("villains", "wt") as fout:
    cout = csv.DictWriter(fout, ["first", "last"])
    cout.writeheader()
    cout.writerows(villains)

with open("villains", "rt") as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)
