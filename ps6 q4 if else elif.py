Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> richter = float(input("Enter a magnitude on the Richter scale: "))
Enter a magnitude on the Richter scale: 8.0
>>> if richter >= 8.0 :
	print("Most structures fall")

Most structures fall
>>> 
elif richter >= 6.0 :
        print("Many buildings considerably damaged, some collapse")
elif richter >= 4.5 :
        print("Damage to poorly constructed buildings")
else:
        print("No destruction of buildings")
        
