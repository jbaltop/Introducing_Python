from collections import defaultdict
def no_idea():
	return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilik'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])
