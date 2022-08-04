class IACSD:
	def __init__(self):
		a="Operating System is a common subject for DITISS,DAC,DBDA"
		print(a)
	def add(self):
		print("=============It is IACSD parent class for Addition===============")
		n= int(input("Enter 1 value for Addition:"))
		m= int(input("Enter 2 value for Adition:"))
		print("Addition of %d and %d is : %d"%(n,m,m+n))
	def call(self):
		print("=========Calling from IACSD Parent Class for Addition===============") 
class DITISS(IACSD):
	def method1(self):
		print(a)
	def mul(self):
		print("================It is DITISS class for multiplication==============")
		n= int(input("Enter 1 value for multiplicaton:"))
		m= int(input("Enter 2 value for multiplication:"))
		print("multiplication of %d and %d is : %d"%(n,m,m*n))
class DAC(IACSD):
	def method2(self):
		print(a)
	def div(self):
		print("================It is DAC class for division==============")
		n= int(input("Enter 1 value for division:"))
		m= int(input("Enter 2 value for division:"))
		if m!=0:
			print("Division of %d and %d is : %d"%(n,m,n/m))
		else:
			print("IT is error")
class DBDA(IACSD):
	def method3(self):
		print(a)
	def sub(self):
		print("================It is DBDA class for substraction==============")
		n= int(input("Enter 1 value for substraction:"))
		m= int(input("Enter 2 value for substraction:"))
		print("substraction of %d and %d is : %d"%(n,m,n-m))
c1=IACSD()
c1.add()
c2=DITISS()
c2.call()
c2.add()
c2.mul()
c3=DAC()
c3.call()
c3.add()
c3.div()
c4=DBDA()
c3.call()
c3.add()
c4.sub()
