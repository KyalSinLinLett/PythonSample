

>>> def concat(*args, sep = "/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>>
>>> def concat(*args, sep = ", "):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth, mars, venus'
>>>
>>> concat("Me", "Myself", "I")
'Me, Myself, I'
>>> def concat(*args, sep = "."):
...     return sep.join(args)
...
>>>
>>> concat("earth", "mars", "venus")
'earth.mars.venus'
>>> concat("earth", "mars", "venus", sep = "#")
'earth#mars#venus'
>>> concat("earth", "mars", "venus", sep = "# ")
'earth# mars# venus'
>>> concat("earth", "mars", "venus", sep = " #")
'earth #mars #venus'
>>> concat("earth", "mars", "venus", sep = "$$")
'earth$$mars$$venus'
>>>
