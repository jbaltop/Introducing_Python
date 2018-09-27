# p271

import dbm

db = dbm.open("output/definitions", "c")

db["mustard"] = "yellow"
db["ketchup"] = "red"
db["pesto"] = "green"

print(len(db))
print(db["pesto"])
db.close()

db = dbm.open("output/definitions", "r")
print(db["mustard"])
db.close()
