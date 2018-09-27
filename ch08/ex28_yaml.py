# p250

import yaml

with open("data/mcintyre.yaml", "rt") as fin:
    text = fin.read()
data = yaml.load(text)
print(data["details"])
print(len(data["poems"]))
print(data["poems"][1]["title"])
