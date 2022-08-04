lst=[]
n=int(input("enter the number: "))
for i in range(0,n):
	i=int(input())
	lst.append(i)
print("original list: ",lst)
lst.reverse()
print("reverse list is : ",lst)
