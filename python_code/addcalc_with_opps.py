a=10
b=20
class calc:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		self.c=50
		self.d=60
		self.cd = self.c
		self.dc = self.d
		self.sum=self.cd+self.dc
		print("Addition of %d, %d is : %d" %(self.cd,self.dc,self.sum))
	def sub(self):
		self.c=self.a-self.b
		print("substraction of %d, %d is : %d" %(self.a,self.b,self.c))
	def mul(self):
		self.c=self.a*self.b
		print("multiplication of %d, %d is : %d" %(self.a,self.b,self.c))
#ob=calc(int(input("enter value of a:")),int(input("enter value of b:")))
ob=calc(a,b)
ob.add()
ob.sub()
ob.mul()
