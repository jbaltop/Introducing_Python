# p192


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(
            "This duck has a",
            self.bill.description,
            "bill and a",
            self.tail.length,
            "tail",
        )


tail = Tail("long")
bill = Bill("wide orange")
duck = Duck(bill, tail)
duck.about()
