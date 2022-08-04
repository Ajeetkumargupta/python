import os
dirname=input("enter directory name: ")
a=os.path.isdir(dirname)
if a==True:
	print("file exits")
else:
	print("file doesn't exit")
	c=os.mkdir(input("enter file name for create a file:"))
	print("Your file  are created")
os.system('pwd')
a=os.system('touch /home/kali/Desktop/python_code/ab/abc.txt')
filename=input("enter your file name: ")
a=os.path.isfile(filename)
if a==True:
	print("file exits")
	abs=os.path.abspath(filename)
	print("absolute path of the file is:",abs)
else:
	print("file doesn't exit")
filename=input("enter file name: ")
a=os.path.exists(dirname)
if a==True:
	print("file exits")
	read=os.access(filename,os.R_OK)
	if read==True:
		print("file having read permission")
	else:
		print("file have not read permission")
else:
	print("file doesn't exit")

