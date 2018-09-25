animal = "fruitbat"


def print_global():
    print("inside print_global:", animal)


print("at the top level:", animal)
print_global()


def change_local():
    animal = "wombat"
    print("inside change_local:", animal, id(animal))


print(change_local())
print(animal)
print(id(animal))
