# for statement

fruits = ['apple', 'banana', 'orange']
for f in fruits:
	print(f, len(f))

# range function

for j in range(10):
	print(j)

# answer: 0,1,2,3 .. 9

for i in range(5, 10):
	print(i)

# answers: 5,6,7,8,9

for i in range(8, 20):
	print(i)

#answers: 8,9,10 ...... 19

a = ['Mary', 'Had', 'A', 'Little', 'Boy']
for i in range(len(a)):
	print(i, a[i])

#answer: 
# 0 Mary
# 1 Had
# 2 A
# 3 Little
# 4 Boy

# prime number tester

for n in range(3, 10):
     for x in range(2, n):
             if n % x == 0:
                     print(n, 'equals', x, '*', n//x)
                     break
     else:
             print(n, 'is a prime number')

for n in range(3, 30):
     for x in range(3, n):
             if n % x == 0:
                     print(n, 'equals', x, '*', n//x)
                     break
     else:
             print(n, 'is a prime number')

#even odd tester

for num in range(2, 20):
     if num % 3 == 0:
             print("Found an even numder", num)
             continue
     print("Found a number", num)