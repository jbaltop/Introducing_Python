# p318

fout = open("output/oops.txt", "wt", encoding="utf-8")
print("Oops, I created a file.", file=fout)
fout.close()
