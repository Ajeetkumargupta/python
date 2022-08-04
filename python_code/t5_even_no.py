lst=[]
n=int(input("Enter the number: "))
for i in range(0,n):
	i=int(input())
	lst.append(i)
print("list: ", lst)
for x in lst:
	if x%2==0:
		print("even no.: ",end='')
		print(x)
