from datetime import date
import getpass
list1=[]
for i in range(0,5):
	i=input("enter 5 first_name:")
	list1.append(i)
list2=[]
for i in range(0,5):
	i=input("enter 5 last_name:")
	list2.append(i)
list3=[]
for i in range(0,5):
	i=input("enter 5 DOB:")
	list3.append(i)
print("first_name_list: ",list1)
print("second_name_list: ",list2)
print("year_born_list: ",list3)
print(date.today())
print(getpass.getuser())
print(list(zip(list1,list2,list3)))
first_latter=list1[0]
space_index=list2.find(" ")
surname=list2[space_index+1:space_index+6]
number=list3[2,3]
username=(first_latter,surname,number)
print(username)
