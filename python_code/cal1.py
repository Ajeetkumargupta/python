#import math
def add(one,two):
        c=float(one)+float(two)
	#c=c+1
        print("Addition of two no.",c)
def sub(one,two):
        c=float(one)-float(two)
       	print("subtraction of two no.",c)

def mul(one,two):
        c=float(one)*float(two)
        print("multiplication of two no.",c)

def div(one,two):
        one = float(one)
        two = float(two)
        if two != 0:
                print("division of two no.",one/two)
        else:
                print("Divide by zero is not possible")
def modulo(one,two):
	TRUE=float(one)%float(two)
	if TRUE==0:
		print(" TRUE %d  modelo of %d "%(one,two))
	else:
		print("%d is not modulo of %d"%(one,two))
def pow(one,two):
	c=float(one)**float(two)
	print("power of %d ^ %d is: %f "%(one,two,c))
def square(one):
	c=float(one)*float(one)
	print("Square of %d is %f"%(one,c))
def s_root(one):
	#print("Enter Value for squareroot: ",math.sqrt(one))
	c=float(one)**0.5
	print("square_root of %d is %f"%(one,c))
def cube(one):
	c=float(one)*float(one)*float(one)
	print("Cube of %d is %f"%(one,c))
def c_root(one):
	c=float(one)**(1/3)
	print("Cube_root of %d is %f"%(one,c))
def ajeet():
	print("Welcome to our calculator")
	print("1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Modulo \n6.Power \n7.square \n8.Square_Root \n9.Cube \n10.Cube_Root\n11.Exit")
	while True:
		choice=input("Enter Any From Above list:")
		if choice in ['1','2','3','4','5','6']:
			#list=[]
			#n=int(input("enter the number: "))
			#for i in range (0,n):
			#	i=int(input())
			#	list.append(i)
			one=(int(input("Enter your first no.:")))
			two=(int(input("Enter your second no.:")))
		if choice=='1':
			add(one,two)
		elif choice=='2':
			sub(one,two)
		elif choice=='3':
			mul(one,two)
		elif choice=='4':
			div(one,two)
		elif choice=='5':
			modulo(one,two)
		elif choice=='6':
			pow(one,two)
		elif choice=='11':
			break
		if choice in ['7','8','9','10']:
			one=(int(input("Enter Your no.")))
		if choice=='7':
			square(one)
		elif choice=='8':
			s_root(one)
		elif choice=='9':
			cube(one)
		elif choice=='10':
			c_root(one)
if __name__=="__main__":
	ajeet()
