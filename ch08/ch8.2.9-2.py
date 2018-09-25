import pickle


class Tiny:
    def __str__(self):
        return "tiny"


obj1 = Tiny()
pickled = pickle.dumps(obj1)
obj2 = pickle.loads(pickled)

print(obj1)
print(str(obj1))
print(pickled)
print(obj2)
print(str(obj2))
