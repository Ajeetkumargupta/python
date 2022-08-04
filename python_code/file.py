import os
input=input("enter file name:- ")
a=os.path.exists(input)
if a==True:
	print("File exists")
	f=open(input,'r')
	print(f.read())
else:
	print("file doesn't exits")
