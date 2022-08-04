import os
filename=input("Enter Filename :-")
a=os.path.exists(filename)
if a==True:
	print("File exist")
	read=os.access(filename,os.R_OK)
	if read==True:
		print("file is having read permission")
	elif read==False:
		print("file doedn't have read permission")
else:
	print("file doesn't exists")
