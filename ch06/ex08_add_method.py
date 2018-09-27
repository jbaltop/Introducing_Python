# p177


class Car:
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()
# give_me_a_car.need_a_push() # AttributeError
