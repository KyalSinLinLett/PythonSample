#week 4b 20-9

fruits = ['orange', 'apple', 'pear', 'banana', 'coconut']
>>> fruits.reverse()
>>> fruits
['coconut', 'banana', 'pear', 'apple', 'orange']

>>> fruits.append('grape')
>>> fruits
['coconut', 'banana', 'pear', 'apple', 'orange', 'grape']

>>> fruits.remove('apple')
>>> fruits
['coconut', 'banana', 'pear', 'orange', 'grape']

>>> fruits.insert(1, 'cucumber')
>>> fruits
['coconut', 'cucumber', 'banana', 'pear', 'orange', 'grape']

>>> fruits.sort()
>>> fruits
['banana', 'coconut', 'cucumber', 'grape', 'orange', 'pear']

>>> fruits.sort(reverse = True)
>>> fruits
['pear', 'orange', 'grape', 'cucumber', 'coconut', 'banana']

>>> fruits.pop()
'banana'

>>> fruits.insert(1, 'orange')
>>> fruits
['pear', 'orange', 'orange', 'grape', 'cucumber', 'coconut']

>>> fruits.remove('orange')
>>> fruits
['pear', 'orange', 'grape', 'cucumber', 'coconut']

>>> fruits.clear()
>>> fruits
[]
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'coconut']
>>> fruits
['orange', 'apple', 'pear', 'banana', 'coconut']
>>>
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

>>> fruits.append('apple')
>>> fruits.append('app;e')
>>> fruits.append('appe')
>>> fruits.append('apple')

>>> fruits.index('apple', 2)
5

>>> fruits.count('apple')
4

>>> fruits.copy()
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple', 'app;e', 'appe', 'apple']
>>> fruits[:]
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple', 'app;e', 'appe', 'apple']
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple', 'app;e', 'appe', 'apple']

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Micheal"])
>>> queue.append("Terry")
>>> queue.popleft()
'Eric'
 defined
>>> queue
deque(['John', 'Micheal', 'Terry'])


>>>
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

>>> i = 6
>>> [str(round(pi, i))]
['3.141593']
>>> [str(round(pi, 0))]
['3.0']
>>> [str(round(pi, _))]

>>> import math as m
>>> m.pi
3.141592653589793
>>> m.pi(16)


>>> matrix = [
...     [1, 2, 3, 4],
...     [5 ,6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>>

>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>>