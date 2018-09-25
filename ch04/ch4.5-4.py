accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation: # 혹은 for card in accusation.keys():
	print(card)
for value in accusation.values():
	print(value)
for item in accusation.items():
	print(item)
for card, contents in accusation.items():
	print('Card', card, 'has the contents', contents)
