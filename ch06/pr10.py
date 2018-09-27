# p196


class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        msg = """laser: %s
claw: %s
smartphone: %s"""

        return msg % (self.laser.does(), self.claw.does(), self.smartphone.does())


robot = Robot()
print(robot.does())
