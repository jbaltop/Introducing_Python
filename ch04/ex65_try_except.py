# p149

short_list = [1, 2, 3]
while True:
    value = input("Position [q to quit]? ")
    if value == "q":
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print("Bad index:", position)
    except Exception as other:
        print("Something else broke:", other)
