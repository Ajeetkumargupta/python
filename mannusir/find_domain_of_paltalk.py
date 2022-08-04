#!/usr/bin/python
#import regular expression
import re
def main():
#open the file with re
	file1=open("Video Chat _ Paltalk.html","r")
#find the xyz.paltalk.com from file file1
	file2=re.findall(r'\w+\.paltalk.com',file1.read())
#we will remove the duplicacy and sort the string
	x=sorted(set(file2))
#use for loop for print in separate line
	for i in x:
		print(i)

if __name__=='__main__':
	main()
