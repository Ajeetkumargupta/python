lst=[]
n=int(input("enter the number: "))
for i in range(0,n):
	i=int(input())
	lst.append(i)
print("list is ", lst)
for n in lst:
	if n%2!=0:
		print("Odd_no: ",end=' ')
		print(n)
