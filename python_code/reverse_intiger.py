a=int(input("Enter the number: "))
reverse=0
while (a>0):
	b=a % 10
	reverse=(reverse*10) + b
	a=a//10
print("reverse number", reverse)

