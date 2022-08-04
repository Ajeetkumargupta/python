#def pal(num):
#	x1 = num[::-1]
#	if x1 == x1:
#		print('palindrome')
#	else:
#		print('not a palindrome')
#print(pal(input("Enter palindrome no:")))


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
