# p284

books = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''

with open("output/books.csv", "wt", encoding="utf-8") as fout:
    fout.write(books)
