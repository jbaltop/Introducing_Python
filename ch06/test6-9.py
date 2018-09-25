class Bear():
	def eats(self):
		return 'berries'

class Rabbit():
	def eats(self):
		return 'clover'

class Octothorpe():
	def eats(self):
		return 'campers'

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())
