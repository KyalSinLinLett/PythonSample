# function that returns a 
# list of numbers of the Fibonnaci series

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

fib2(400)

# function that prints out the Fibonnaci series
# to the nth

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a + b
	print()

fib(100)

# defining scope

i = 5

def f(arg=i)
	print(arg)

# Keyword arguments

def parrot(voltage = 10000, state = "a stiff", action = 'voom', type = 'bird'):
	print("This parrot wouldn't ", action, end = '')
	print("if you put ", voltage, " volts through it.")
	print("Lovely plumage, the ", type)
	print("Its ", state, " !" )

parrot(voltage = 10)
parrot(10, 'dead', 'jump', 'bird')








