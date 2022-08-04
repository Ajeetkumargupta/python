import os
input=input("enter directory name:- ")
a=os.path.isdir(input)
if a==True:
	print("Directory are exist")
else:
	print("Directory are not exist")
