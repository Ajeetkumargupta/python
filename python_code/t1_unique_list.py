# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	i = int(input())

	lst.append(i) # adding the element
lst_set = len(set(lst))
#number_of_unique_values = len(lst_set)
#print("number_of_unique_values",number_of_unique_values)
print("number_of_unique_values",lst_set)
print(lst)
print(type(lst))


#a_list = [1, 1, 2, 2, 3]
#a_set = set(a_list)
#number_of_unique_values = len(a_set)
#print(number_of_unique_values)
