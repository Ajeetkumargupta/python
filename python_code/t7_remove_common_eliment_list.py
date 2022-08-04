lst=[]
lst1=[]
n=int(input("Enter a number: "))
for i in range(0,n):
	i=int(input())
	lst.append(i)
m=int(input("Enter a number: "))
for i in range(0,m):
       	i=int(input())
       	lst1.append(i)
print("list1: ",lst)
print("list2: ",lst1)
new_list=set(lst) - set(lst1)
final_list=lst+list(new_list)
print("without coomon value",final_list)


