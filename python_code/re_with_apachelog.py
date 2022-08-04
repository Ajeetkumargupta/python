import re
file1=open('apache_log.py','r')
file2=re.findall(r'\d+\.\d+\.\d+\.\d+',file1.read())
print(file2)
print("=====================================================================")
print("UNIQUE IP FROM GIVEN IP'S")
set1=set(file2)
print(set1)
