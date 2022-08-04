import os
filename=input("Enter File Name:-")
a=os.path.isfile(filename)
if a==True:
	print("file exist")
	abs=os.path.abspath(filename)
	print("Absolute path of the filenam is",filename,abs)
else:
	print("file doesn't exists")
