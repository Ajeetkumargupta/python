#!/usr/bin/python	
#---------------> shebang

#This is main () function

#======================================
def main():
	print("Hello World!!!!!!!!!")

#boilerplate code
if __name__=='__main__':
        main()


#======================================
def tinku():
	print("Hello World!!!!!!!!!")

def main():
	tinku()
	print(tinku()) # here print nono bcz nothing print in tinku 

#boilerplate code
if __name__=='__main__':
	main()


#================================

a=[10,20,30,40]
print(a)
a.append(50)
print(a)
b=a.append(60)
print(a)
print(b) #-------> print none


#====================================

var1=True
var2=False
print(type(var1))
print(type(var2))

#====================================
a='ajeet'
b='abc'
print(a==b)


#===================================

a="UTTAR PRADESH"
for ajeet in a:
	print(ajeet)

#====================================

a=[7,20,33,22,44,100]
print (99 in a)
print (7 in a)
