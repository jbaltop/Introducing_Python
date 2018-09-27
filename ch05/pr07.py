# p169

from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists["a"].append("something for a")
print(dict_of_lists["a"])
