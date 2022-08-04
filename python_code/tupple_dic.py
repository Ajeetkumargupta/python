#salaries={}
#salaries[('tinku_sharma')] =10000
#salaries[('gabbar_singh')] =20000
#print(salaries)

#i=input("enter user name: ")
#if i in salaries:
#	print ("tinku_sharma")
#else:
#	print("user not found")

#print(salaries.keys())

#==================================

#A=(1,2,3,4,5)
#A=('a','b','c','d','e')
#print(A)
#print(type(A))
#print(len(A))


#================================
#sequence unpacking
#student=('Ajeet','Gupta',223403,'Ditiss')
#student1=('rishu','yadav',223437,'Ditiss')
#print(student)
#print(type(student))
#fname,lname,roll_no,branch = student
#print("=================================")
#print(fname)
#print(roll_no)
#print("=================================")

#fname,lname,roll_no,branch = student1
#print(fname)
#print(roll_no)
#print(type(student))
#Student=list(student)
#print("=================================")

#print(Student)
#print(type(Student))

#STUDENT=tuple(Student)
#print("=================================")

#print(STUDENT)
#print(type(STUDENT))


#=======================================================
#dictonry with charector key
#empty dict
#a={}
#a['a']='apple'
#a['b']='banana'
#a['c']='campus'
#a['d']='data'
#print(a)
#print(type(a))

#====================================

#dictonry with number key

#a={}
#a[1]='ajeet'
#a[2]='kumar'
#a[3]='gupta'
#print(a)
#print(type(a))
#print(a[2])
#it will give keys_error because 4 are not key 
#print(a[4])


#====================================================

dict={2:20,3:30,5:50,1:10,4:40}
print(dict)
print(type(dict))
print(sorted(dict.keys()))
print(sorted(dict))
print(type(sorted(dict)))

for i in sorted(dict):
	print(i,dict[i])
print(dict)
print(dict.items())
print(type(dict.items()))
