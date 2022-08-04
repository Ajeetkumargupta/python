import re
def ajeet(a,b):
	match=re.search(a,b)
	if match:
		print(match.group())
	else:
		print("pattern not found")
ajeet(input("enter pattern:"),input("enter text:"))
#find('is','ditiss')
#=========================================
#import re
#def find(pat,text):
#	match=re.search(pat,text)
#	if match:
#		print(match.group())
#	else:
#		print("pattern not found")
#find(r'is','ditiss')
