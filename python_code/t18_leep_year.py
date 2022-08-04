n=int(input("enter a number: "))
#if n%4==0:
#	if n%400==0:
#		if n%100==0:
#			print("this year is leep year",n)
#		else:
#			print("this year is not a leep year", n)

#======================================================================
#if n%400==0 and n%100==0:
#	print("this year is leep year".format(n))
#elif n%4==0 and n%100!=0:
#	print("this year is leep year".format(n))
#else:
#	print("this year is leep year".format(n))

#======================================================

if (n%4==0) or (n%100!=0) and (n%400==0):
	print("this year is leep year")
else:
	print("this year is not leep year")
