#class name:
#	firstname='motu'
#	lastname='sharma'
#create a object and call the class which name is name
#object1=name()
#print(name.firstname)
#print(name.lastname)


#===============================================================


class student:
	def __init__(self):
		print("hello")
a=student()

class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
s1=Student('ajeet','24')
print(s1.name,s1.age)
s2=Student('onkar','31')
print(s2.name,s2.age)
s3=Student((input("enter name: ")),int(input("enter age: ")))
print(s3.name,s3.age)
