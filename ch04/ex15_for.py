# p117

accusation = {"room": "ballroom", "weapon": "lead pipe", "person": "Col. Mustard"}
for card in accusation:  # or for card in accusation.keys():
    print(card)

print("-----")

for value in accusation.values():
    print(value)

print("-----")

for item in accusation.items():
    print(item)

print("-----")

for card, contents in accusation.items():
    print("Card", card, "has the contents", contents)
