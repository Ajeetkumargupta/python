
#min = int(input("Enter the min : "))
#max = int(input("Enter the max : "))

#for n in range(min,max + 1):
#for n in range(max + 1):
#   if n > 1:
#       for i in range(2,n):
#           if (n % i) == 0:
#              break
#       else:
#           print(n)


#====================================================

# Program to check if a number is prime or not

num = int(input("Enter the number : "))

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")# Program to check if a number is prime or not

