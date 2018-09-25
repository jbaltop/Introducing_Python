from datetime import date

halloween = date(2015, 10, 31)
items = [halloween, halloween.day, halloween.month, halloween.year, halloween.isoformat()]

for item in items:
	print(item)
