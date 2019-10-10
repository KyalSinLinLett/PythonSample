#week5B



with open('test.txt', 'r') as f:
	#this reads out all the lines
	scopeToRead = 1000
	f_text = f.read(scopeToRead)
	for n in f_text:
		print(n, end='')

	#this just reads out the first line
	f_text = f.readline()
	for n in f_text:
		print(n, end='')

	#this works but ends up with an infinite loop
	while len(f_text) > 0:
		print(f_text, end='')

	#this is the simplest one and the most efficient
	for n in f:
		print(n, end='')


f = open('test.txt', 'r')
print(f.name)

f.close()


