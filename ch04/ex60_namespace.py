# p145

animal = "fruitbat"


def print_global():
    print("inside print_global:", animal)


print("at the top level:", animal)
print_global()


"""should through UnboundLocalError
def change_and_print_global():
    print("inside change_and_print_global:", animal)
    animal = "wombat"
    print("after the change:", animal)
"""


def change_local():
    animal = "wombat"
    print("inside change_local:", animal, id(animal))


change_local()
print(animal)
print(id(animal))
