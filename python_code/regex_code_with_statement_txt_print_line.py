import re
#==========================print no of line=================
f=open('statement.txt','r')
#print(len(f.readlines()))

#========================print start with no ==============
#file=re.findall(r'\d..+',f.read())
#print(file)
#print(len(file))
#========================print start with only special charector=========

#file=re.findall(r'^\W..+',f.read(),re.MULTILINE)
#print(file)

#========================print start with only alphabet===========

#file=re.findall(r'^[a-z,A-Z].+',f.read(),re.MULTILINE)
#print(file)

#========================print start with only vowels===========

file=re.findall(r'^[a,e,i,o,u,A,E,I,O,U].+',f.read(),re.MULTILINE)
print(file)
