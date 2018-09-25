periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)
from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)
