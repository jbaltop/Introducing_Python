# p284

import csv

with open("data/books.csv", "rt") as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)
