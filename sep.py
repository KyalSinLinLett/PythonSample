#Week3A Cancel
#Week3B 13.9.2019

#Arbitrary Argument Lists
>>> args = [1, 10]
>>> list(range(*args))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>>


#Lambda Functions
>>> def make_incrementer(n):
...     return lambda x: x + n
...
>>> f = make_incrementer(42)
>>> f(0)
42
>>> f(1)
43

