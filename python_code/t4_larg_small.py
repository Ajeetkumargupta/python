lst=[]
n=int(input("enter the number: "))
for i in range(0,n):
	i=int(input())
	lst.append(i)
print("list: ",lst)
print("largest_no in list: ",max(lst))
print("smallest_no in list: ",min(lst))
