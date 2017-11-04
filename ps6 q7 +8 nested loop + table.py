Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(3):
	for j in range(1,4):
		print(i+j,end="")

		
123234345
>>> print()

>>> 
>>> 
>>> print("%11s"%"1","%9s"%"2","%9s"%"3")
          1         2         3
>>> print("%10s"%"x","%9s"%"x","%9s"%"x")
         x         x         x
>>> print("\t---------------------------")
	---------------------------
>>> for i in range(1,6):
	for j in range(1,4):
		print("%10d"%(i**j),end="")
		print()

	
         1
         1
         1
         2
         4
         8
         3
         9
        27
         4
        16
        64
         5
        25
       125
>>> 
