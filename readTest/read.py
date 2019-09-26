f = open('test.txt', 'r')
print(f.read())
f.closed	

with open('test.txt') as f:
	read_data = f.read()
	print(read_data)
f.closed