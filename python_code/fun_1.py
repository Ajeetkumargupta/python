#def fun(v):
#a=['ajeet','kumar']
#	print(v)
#fun(123)

#===================================

a={1:'ajeet',2:'kumar',3:'gupta'}
print(a)
print(type(a))
print(sorted(a.items()))
print(type(sorted(a.items())))

print("====================== next=================")

#def fun(x):
#	return(x[1])
#print(fun(1:'ajeet'))
#print(square.__doc__)

print("====================== next=================")

def square(x):
	'''It is a square function!!!!!!!!'''
	sq=x*x
	print("square of %d is %d" %(x,sq))
square(int(input("enter a number: ")))

help(square)
