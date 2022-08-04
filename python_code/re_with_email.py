import re
abc=open('mail.txt','r')
#file = re.findall(r'user', abc.read())
#print(file)
file=re.findall(r'\s\w+@\w+\.\w+',abc.read())
#file=re.findall(r'\s\w+\W\w+\.\w+',abc.read())
print(list(file))
