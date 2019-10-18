# example 1
class Employee:
	 empCount = 0

	 def __init__(self, name, salary):
	 	self.name = name
	 	self.salary = salary
	 	Employee.empCount += 1

	 def displayCount(self):
	 	print("Total Employee %d" % Employee.empCount)

	 def displayEmployee(self):
	 	print("Name : {}, Salary : {}".format(self.name, self.salary))

emp1 = Employee("Zara", 2000)
emp1.displayEmployee()
emp2 = Employee("Manni", 3500)
emp2.displayEmployee()
print("The number of employee(s):", Employee.empCount)


