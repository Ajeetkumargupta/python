class Employee:
	def __init__(self,Employeecode,fname,lname,gender,address,salary):
		self.Employeecode=Employeecode
		self.fname=fname
		self.lname=lname
		self.gender=gender
		self.address=address
		self.salary=salary
s1=Employee(1001,'Ajeet','gupta','Male','U.P.',500000)
s2=Employee(1002,'rishi','yadav','Male','U.P.',500000)
s3=Employee(1003,'omkar','kk','Male','MH.',50000)
s4=Employee(1004,'mithilesh','bhardhvaj','Male','U.P.',500000)
s5=Employee(1005,'prathamesh','kalpe','Male','MH.',400000)
s6=Employee(1006,'Atharv','kulkarni','Male','MH.',300000)
s7=Employee(1007,'Akash','gupta','Male','MH',5000)
s8=Employee(1008,'mohit','chacha','Male','M.P.',500000)
s9=Employee(1009,'Anchal','gupta','female','U.P.',500000)
s10=Employee(1010,'vikash','unknown','Male','U.P.',50000)

print("EmployeeID Is:- %d, Firstname Is:- %s,Lastname Is:- %s,Gender Is:- %s,Address Is:-%s,Salary Is: %d" %(s1.Employeecode,s1.fname,s1.lname,s1.gender,s1.address,s1.salary))
