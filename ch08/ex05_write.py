# p234

try:
    fout = open("output/relativity", "xt", encoding="utf-8")
    fout.write("stomp stomp stomp")
except FileExistsError:
    print("relativity already exists!. That was a close one.")
