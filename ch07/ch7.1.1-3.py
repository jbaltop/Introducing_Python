#!/usr/local/bin/python3

place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

place4 = place_bytes.decode('latin-1')
print(place4)

place5 = place_bytes.decode('windows-1252')
print(place5)
