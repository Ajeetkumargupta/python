#from math import factorial
#import math
#a=int(input("Enter a number:- "))
#print(factorial(a))

#==================================

num = int(input("enter a number: "))
  
fact = 1
i = 1
  
while i <= num:
 fact = fact * i
 i = i + 1
  
print ("Factorial of the number %d is %d" %(num, fact))
