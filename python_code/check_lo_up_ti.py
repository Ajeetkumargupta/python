a=input("enter a sting :- ")

if (a.islower()):
	print("it is lower case")
elif(a.isupper()):
	print("IT IS UPPER CASE")
elif(a.istitle()):
	print("It Is Title Case")
else:
	print(" It is caseless")
	print("we will convert into upper",a.upper())
