# p194

from collections import namedtuple

Duck = namedtuple("Duck", "bill tail")
duck = Duck("wide orange", "long")

print(duck)
print(duck.bill)
print(duck.tail)

duck2 = Duck(bill="wide orange", tail="long")
print(duck2)

duck3 = duck2._replace(tail="magnificent", bill="crushing")
print(duck3)

duck_dict = {"bill": "wide orange", "tail": "long"}
print(duck_dict)

duck_dict["color"] = "green"
print(duck_dict)

# duck.color = 'green' # AttributeError
