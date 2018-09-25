poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night."""

print(len(poem))

fout = open("relativity", "wt")
print(fout.write(poem))
fout.close()

fout = open("relativity", "wt")
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(poem[offset : offset + chunk]))
    offset += chunk
fout.close()

try:
    fout = open("relativity", "xt")
    fout.write("stomp stomp stomp")
except FileExistsError:
    print("relativity already exits!. That was a close one.")
