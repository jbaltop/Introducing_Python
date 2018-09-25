from collections import defaultdict

food_counter = defaultdict(int)
for food in ["spam", "spam", "eggs", "spam"]:
    food_counter[food] += 1
for food, count in food_counter.items():
    print(food, count)
