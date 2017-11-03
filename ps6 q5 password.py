Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> set_password = "changeme"
>>> attempts = 0
>>> while True:
	password = input("Enter password: ")
	attempts+=1
	if password == set_password:
		print("Password accepted")
		break
	else:
		print("Incorrect password")
		if attempts>5:
			print("Exceeded attempts,Accessed Denied")
			break
		print("You had " +str(attempts) +" attempts to guess the password")
		
