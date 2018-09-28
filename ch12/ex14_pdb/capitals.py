# p414

"""usage
$ python capitals.py ../data/cities1.csv
$ python capitals.py ../data/cities2.csv
$ python -m pdb capitals.py ../data/cities2.csv
(set breakpoint at `return  # set breakpoint here`)
"""


def process_cities(filename):
    with open(filename, "rt", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "quit" in line.lower():
                return  # set breakpoint here
            country, city = line.split(",")
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=",")


if __name__ == "__main__":
    import sys

    process_cities(sys.argv[1])
