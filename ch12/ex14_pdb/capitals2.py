# p418

"""usage
$ python capitals2.py ../data/cities1.csv
$ python capitals2.py ../data/cities2.csv
"""


def process_cities(filename):
    with open(filename, "rt", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "quit" == line.lower():
                return
            country, city = line.split(",")
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=",")


if __name__ == "__main__":
    import sys

    process_cities(sys.argv[1])
