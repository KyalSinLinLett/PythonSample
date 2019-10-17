class Dog:
# 	kind = "Canine"
# 	walks_on = "four legs"

# 	def __init__(self, name, fur_colour, fur_type):
# 		self.name = name
# 		self.fur_colour = fur_colour
# 		self.fur_type = fur_type


# d = Dog('Fido', 'Brown', 'straight and long')
# e = Dog('Buddy', 'White', 'curly')

# print(d.kind, d.walks_on)
# print(e.kind, e.walks_on)

# print(d.name, d.fur_colour, d.fur_type)
# print(e.name, e.fur_colour, e.fur_type)

	def __init__(self, name):
		self.name = name
		self.tricks = []

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('EDDIE')
e = Dog('GEORGIE')

d.add_trick('shake paw')
e.add_trick('fetch newspaper')

d.add_trick('play dead')

print(d.tricks)
print(e.tricks)
