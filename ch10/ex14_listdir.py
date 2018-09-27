# p322

import os

os.mkdir("output/poems")
print(os.listdir("output/poems"))
os.mkdir("output/poems/mcintyre")
print(os.listdir("output/poems"))

fout = open("output/poems/mcintyre/the_good_man", "wt", encoding="utf-8")
fout.write(
    """Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
"""
)
fout.close()

print(os.listdir("output/poems/mcintyre"))
