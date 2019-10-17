# Exceptions self study

# x = 10
# if x > 5:
# 	raise Exception("The number cannot exceed 5. You entered {}.".format(x))

# ----- assertion error -----

# import sys
# assert('linux' in sys.platform), "This code runs only on Linux"
# import sys
# def linux_interaction():
# 	assert('linux' in sys.platform), "This function only runs on Linux systems"
# 	print("Hey! User.")

# try:
# 	linux_interaction()
# except AssertionError as error:
# 	print(error)
# 	

# ----- file i/o, filenotfounderror -----

# try:
# 	linux_interaction()
# except FileNotFoundError as fnf_error:
# 	print(fnf_error)
# except AssertionError as ass_error:
# 	print(ass_error)
# 	print('Linux linux_interaction() function was not executed')
# else:
# 	print("You have made no effort my dude, you are pathetic.")

# import time


# try:
# 	linux_interaction()
# except AssertionError as error:
# 	print(error)
# else:
# 	try:
# 		with open('file.log') as file:
# 			read_data = file.read()
# 	except FileNotFoundError as fnf_error:
# 		print(fnf_error)
# finally:
# 	print("This exception handling code has run, you are in the finally block. This is the end of the exception handling")

# ----- IO Error -----
# import time

# try:
# 	file = open('file.txt', 'r')
# except IOError:
# 	print("File not found")
# else:
# 	print("File is opened successfully")
# finally:
# 	time.sleep(5)
# 	print("The code has run successfully")

# ----- Throwing multiple exceptions -----

# import time

# try:
# 	a = 10/0
# 	print(a)
# # except ArithmeticError:
# # 	print("Arithmetic error has occured")
# except ZeroDivisionError:
# 	print("You cannot divide by zero, idiot!")
# else:
# 	print("Division is successful")
# finally:
# 	time.sleep(5)
# 	print("\nsuccessfully completed dividing task")

# ----- Raising exceptions -----

# try:
# 	age = int(input("Enter your age: "))
# 	if age < 18:
# 		raise ValueError
# 	else:
# 		print("The age is valid, welcome to the big bois club!")
# except ValueError:
# 	print("The age is invalid")

# a = int(input('Enter int a: '))
# b = int(input('Enter int b: '))

# try:
# 	if b is 0:
# 		raise ArithmeticError
# 	else:
# 		print("a/b is ", a/b)
# except ArithmeticError:
# 	print("The value of b cannot be zero! You cannot divide shit with zero you fucking idiot!")

# an alternative case if raise isnt used

# a = int(input('Enter int a: '))
# b = int(input('Enter int b: '))

# try:
# 	ans = a/b
# except ArithmeticError as AR_Error:
# 	print("The divisor cannot be zero!")
# else:
# 	print("The answer is ", ans)
# finally:
# 	print("The code has ran successfully")
# 	

# ----- Custom Exception -----

# class ErrorInCode(Exception):
# 	def __init__(self, data):
# 		self.data = data
# 	def __str__(self):
# 		return repr(self.data)

# try:
# 	raise ErrorInCode(2000)
# except ErrorInCode as ae:
# 	print("Received error: ", ae.data)


# class Complex:
# 	def __init__(self, realp, imagp):
# 		self.r = realp
# 		self.i = imagp

# x = Complex(3.0, -4.5)
# print(x.r, x.i)