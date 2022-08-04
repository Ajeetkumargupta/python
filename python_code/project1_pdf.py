from datetime import date
import getpass
print(getpass.getuser())
print("Ajeet kumar gupta")
print("today_Date: ",date.today())
#==========================
print("duscription of program: ", 'This program is define in sections')
#=======================
f=float(input("Enter the fahrenheit number: " ))
c=((f-32)*5/9) 
print("this is celsius",c)

#=============================
n=input("Enter the string: ")
print("IN UPPER LATTER: ",n.upper())
print("in lower latter",n.lower())
print("In Title Latter",n.title())
#============================
print(len(n))
#=============================
n=input("enter a string:")
f="I am Ajeet Kumar Gupta"
print("THIS is F string: ",f)
l=n+f
print("Assign string with f: ",l)
