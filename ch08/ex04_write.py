# p234

poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night."""

fout = open("output/relativity", "wt", encoding="utf-8")
size = len(poem)
offset = 0
chunk = 100

while True:
    if offset > size:
        break
    print(fout.write(poem[offset : offset + chunk]))
    offset += chunk

fout.close()
