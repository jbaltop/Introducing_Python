# p284

books2 = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""

with open("output/books2.csv", "wt", encoding="utf-8") as fout:
    fout.write(books2)
