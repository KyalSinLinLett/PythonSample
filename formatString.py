#week5A 26.9.2019

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
	

animals = { 'Tiger'  : 3000,
			'Lion'   : 3822,
			'Leopard': 400
			}

for animals, amount in animals.items():
	print(f'{animals:1} ==> {amount:1d}')

bird = 'sparrow'

print(f'My plane hits {bird} over the cloud.')
print(f'{bird}{bird}My plane hits {bird!r} over the cloud')

# The string format
print('We are the {} who say" {}!"'.format('Knights', 'Nee'))

# print(f'This {food} is {adjective}{object}'.format(food = 'spam', adjective = 'absolutely', object = 'good'))


for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

f = open('workfile', 'w')

with 