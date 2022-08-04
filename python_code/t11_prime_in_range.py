n=int(input("enter a minimum range of prime number: "))
m=int(input("enter a maximum range of prime number: "))
for i in range(n,m+1):
	if i>1:
		for j in range(2,i):
			if i%j==0:
				print("Not prime",i)
				break
		else:
			print("It is prime",i)
