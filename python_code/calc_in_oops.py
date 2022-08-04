class calc:
	def __init__(self):
		print("Welcome to the our calculator")
		print("1.Addition")
		print("2.Substraction")
		print("3.MUltiplication")
		print("4.Division")
		print("5.Square")
		print("6.Square_root")
		print("7.Cube")
		print("8.Cube_root")
		print("11.Exit")
		while True:
			choice = input("Enter Your Choice:")
			if choice=='1':
				self.add()
			elif choice=='2':
				self.sub()
			elif choice=='3':
				self.mul()
			elif choice=='4':
				self.div()
			elif choice=='5':
				self.square()
			elif choice=='6':
				self.sq_root()
			elif choice=='7':
				self.cube()
			elif choice=='8':
				self.cube_root()
		while False:
			choice = '11'
			break
	def add(self):
		a=int(input("enter your first no: "))
		b=int(input("enter your second no: "))
		print("Addition of %d and %d is: %d "%(a,b,a+b))
	def sub(self):
		a=int(input("enter your first no: "))
		b=int(input("enter your second no: "))
		print("Substraction of %d and %d is: %d "%(a,b,a-b))
	def mul(self):
		a=int(input("enter your first no: "))
		b=int(input("enter your second no: "))
		print("MULtiplication of %d and %d is: %d "%(a,b,a*b))
	def div(self):
		a=int(input("enter your first no: "))
		b=int(input("enter your second no: "))
		if b>0:
			print("Division of %d and %d is: %d "%(a,b,a/b))
		else:
			print("Undetermine")
	def square(self):
		a=int(input("enter no. for square: "))
		print("Square of %d is :%d"%(a,a*a))
	def sq_root(self):
		a=int(input("enter no. square_root: "))
		print("Square_root of %d  is: %d "%(a,a**0.5))
	def cube(self):
		a=int(input("enter no. for cube: "))
		print("cube of %d  is: %d "%(a,a*a*a))
	def cube_root(self):
		a=float(input("enter no. for cube_root: "))
		print("cube_root of %d  is: %f "%(a,float(a**(1/3))))
s1=calc()
s1.add()
s1.sub()
s1.mul()
s1.div()
s1.square()
s1.sq_root()
s1.cube()
s1.cube_root()
