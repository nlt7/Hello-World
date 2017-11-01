Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from math import sqrt
>>> X = 2
>>> Y = 4
>>> print("the product of",x,"and",y,"is",x+y)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("the product of",x,"and",y,"is",x+y)
NameError: name 'x' is not defined
>>> print("the root of their differences is ",sqrt(x-y))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("the root of their differences is ",sqrt(x-y))
NameError: name 'x' is not defined
>>> print("the root of their difference is",sqrt(x-y))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("the root of their difference is",sqrt(x-y))
NameError: name 'x' is not defined
>>> 
