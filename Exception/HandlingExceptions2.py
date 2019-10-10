# import sys

# try:
# 	f = open('myFile.txt')
# 	s = f.readline()
# 	i = int(s.strip())
# except OSError as err:
# 	print("OS error: {0}".format(err))
# except ValueError:
# 	print("Couldn't convert data to an integer.")
# except:
# 	print("Unexpected error: ", sys.exc_info()[0])
# 	raise

# try...except statement

# try:
# 	text = input("Enter something: ")
# except EOFError:
# 	print("Why did you do an EOF on me?")
# except KeyboardInterrupt:
# 	print("You canceled the operation.")
# else:
# 	print("You entered {}".format(text))

# Raising Exceptions

# class ShortInputException(Exception):
# 	'''A user defined exception class'''
# 	def __init__(self, length, atleast):
# 		Exception.__init__(self)
# 		self.length = length
# 		self.atleast = atleast

# try:
# 	text = input("Enter something -->")
# 	if len(text) < 3:
# 		raise ShortInputException(len(text), 3)
# 		#other work can continue as usual here

# except EOFError:
# 	print("Why did you do an EOF on me?")

# except ShortInputException as ex:
# 	print(('ShortInputException: The input was ' + 
# 		'{0} long, expected at least {1}').format(ex.length, ex.atleast))
# else:
# 	print("No exception was raised")

# try...finally
import sys
import time

f = None
try:
	f = open("poem.txt")
	# our usual file-reading idiom

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		
		print(line, endl='')
		sys.stdout.flush()
		print("Press ctrl+c now")

		# to make sure it runs for awhile
		# time.sleep(2)

except IOError:
	print("Could not find file poem.txt")

except KeyboardInterrupt:
	print("!! you canceled the reading from the file.")

finally:
	if f:
		f.close()
	print("(Cleaning up: closed the file)")