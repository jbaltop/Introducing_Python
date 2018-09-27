# p339

from datetime import date

today = date.today()
with open("output/today.txt", "wt", encoding="utf-8") as fout:
    fout.write(str(today))
