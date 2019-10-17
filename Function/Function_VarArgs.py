# VarArgs parameters

# def total(a = 5, *numbers, **phonebook):
# 	print('a', a)

# 	for single_items in numbers:
# 		print('single_items', single_items)

# 	for first_part, second_part in phonebook.items():
# 		print(first_part, second_part)

# total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1459)

# def studentbook(*numbers, **contact):

# 	for single_num in numbexrs:
# 		print('single_num =', single_num)

# 	for contact_name, contact_num in contact.items():
# 		print(contact_name, contact_num)

# studentbook(1, 3, 4, 63, Mg=1102, Aye=2203, Aung=449)

# Return statement

# def maximum(x, y):
# 	if x > y:
# 		return x
# 	elif x == y:
# 		return 'The numbers are equal'
# 	else: 
# 		return y

# print(maximum(3, 8))

# DOC string (Documentation string)

def print_max(x, y):
	'''1. Prints the maximum of two numbers
The two values must be integers
	'''
	'''2. Prints the maximum of two numbers
The two values must be integers
	'''

# 	x = int(x)
# 	y = int(y)

# 	if x > y:
# 		print(x, "is maximum")
# 	else:
# 		print(y, "is maximum")

# print_max(5, 9)
print(print_max.__doc__)

# # from time import sleep
# # print(sleep.__doc__)
# import time
# import math
# import random
# print(time.__doc__)
# print(random.__doc__)

print(__doc__.__doc__)


