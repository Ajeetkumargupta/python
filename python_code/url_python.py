import re
from urllib.request import urlopen
#webpage=urlopen("https://docs.python.org/3/download.html")
#print(webpage.read().decode("utf-8"))
#print(type(webpage.read().decode("utf-8")))
#file=urlopen("https://docs.python.org/3/download.html").read().decode("utf-8")
file=urlopen(input("Enter url link of any website:")).read().decode("utf-8")
print(file)
print(type(file))
list=re.findall("<title.*?>.*?</title.*?>",file,re.MULTILINE)
print(list)
#print("Title of the website is : ")
#print (file.title.string)

#list=re.findall(r'^<title>..</title>',file())
#print(list)
