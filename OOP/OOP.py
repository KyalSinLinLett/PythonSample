#18.10.2019

# Classes

# class Person:
# 	pass # An empty block

# p = Person()
# print(p)

# Methods

# class Person:
# 	def say_hi(self):
# 		print('Hello, how are you?')

# p = Person()
# p.say_hi()

# __init__ method

# class Person:
# 	def __init__(self, name):
# 		self.name = name
# 	def say_hi(self):
# 		print('Hello, my name is', self.name)

# p = Person('Swaroop')
# p.say_hi()

# class Student:
# 	def __init__(self, name, student_card):
# 		self.name = name
# 		self.student_card = student_card

# 	def show_student(self):
# 		print('Student name is {} and student card 
# 			number is {}'.format(self.name, self.student_card))

# std1 = Student('Maung Maung', '10001')
# std1.show_student()

# dog = Dog('name', '')
# dog.color
# dog.owner
# dog.functions - bark, eat, sleep, bite

# class Dog:
# 	def __init__(self, name, color, owner):
# 		self.name = name
# 		self.color = color
# 		self.owner = owner

# 	def bark(self):
# 		print("{} is barking.".format(self.name)")

# 	def eat(self):
# 		print("{} is eating food.".format(self.name))

# 	def sleep(self):
# 		print('{} is sleeping...'.format(self.name))

# 	def bite(self):
# 		print('{} is biting you!'.format(self.name))

# d1 = Dog('Bobby', 'Black', 'John Smith')
# print(d1.name, d1.color, d1.owner)
# d1.bark()
# d1.eat()
# d1.sleep()
# d1.bite()

# Class And Object Variables

# class Robot:
# 	"""Represents a robot, with a name."""
# 	population = 0

# 	def __init__(self, name):
# 		"""Initialize the data."""

# 		self.name = name
# 		print("(Initializing {})".format(self.name))

# 		Robot.population += 1

# 	def die(self):
# 		"""I am dying."""

# 		print("{} is being destroyed!".format(self.name))

# 		Robot.population -= 1

# 		if Robot.population == 0:
# 			print("{} was the last one.".format(self.name))
# 		else:
# 			print("There are still {:d} robots working.".format(Robot.population))

# 	def say_hi(self):
# 		"""Greeting by the robot.
# 		Yeah, they can do that."""
# 		print('Greetings, my sister call me {}'.format(self.name))

# 	@classmethod
# 	def how_many(cls):
# 		"""Prints the current population"""
# 		print("We have {:d} robots.".format(cls.population))


# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# print("\n Robots can do some work here.\n")

# print("Robots have finished their work, So, let's destroy them")
# droid1.die()
# droid2.die()

# Robot.how_many()


# name age status functions

# how many dogs
# living
# functions
# when he die
# how many dogs left

# class Dog:

# 	dog_count = 0

# 	def __init__(self, name, born):
# 		self.name = name
# 		self.born = born
# 		print("A new dog is adopted!")

# 		Dog.dog_count += 1

# 	def say_hi(self):
# 		print("The dog name is {}.".format(self.name))
# 		print("The dog is born in {}".format(self.born))

# 	def die(self, death_month):
# 		self.death_month = death_month

# 		Dog.dog_count -= 1

# 		print('{} died in {}'.format(self.name, self.death_month))

# 		if Dog.dog_count == 0:
# 			print("This was the last dog!")
# 		else:
# 			print("There are still {:d} dogs left.".format(Dog.dog_count))

# 	def functions(self):
# 		print("The {} can bark".format(self.name))
# 		print("The {} can bite".format(self.name))
# 		print("The {} can eat".format(self.name))
# 		print("The {} can sleep".format(self.name))

# 	@classmethod
# 	def how_many(cls):
# 		print("We have {:d} dogs".format(cls.dog_count))

# dog1 = Dog('George', 'January')
# dog1.say_hi()
# Dog.how_many()

# dog2 = Dog('Bob', 'March')
# dog2.say_hi()
# Dog.how_many()

# dog1.functions()
# dog2.functions()
# print('\nThe dogs have died\n')
# dog1.die('May')
# dog2.die('April')

# Dog.how_many()

# Inheritance
class SchoolMember:
	"""Represents any school member"""

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("(Initialized school member: {})".format(self.name))

	def tell(self):
		"""Tell my details."""
		print('Name: "{}", Age:"{}"'.format(self.name, self.age), end='')

class Teacher(SchoolMember):
	'''Represents a student.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized teacher: "{}"'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

class Student(SchoolMember):
	'''Represents a student'''
	def __init__(self, name, age, marks, studentID):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		self.studentID = studentID
		print('(Initialized student: "{}"'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print(' Marks: "{}, StudentID: "{}""'.format(self.marks, self.studentID))

class Headmaster(SchoolMember):
	'''Represents a headmaster'''
	def __init__(self, name, age, position):
		SchoolMember.__init__(self, name, age)
		self.position = position
		print('(Initialized headmaster): "{}"'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print(' Position: {}'.format(self.position))

t = Teacher("Mrs. Shrividya", 40, 30000)
s = Student("Swaroop", 25, 75, 'A1100')
h = Headmaster('Mr. George', 55, 'Headmaster')

print()

members = [t, s, h]
for member in members:
	member.tell()






