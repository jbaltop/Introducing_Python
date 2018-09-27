# p183


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

# c.diameter = 20 # AttributeError
