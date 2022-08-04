#/usr/bin/python3

import sys
def main():
	print(sys.argv)
	print("you have enter",sys.argv[1],sys.argv[2])
	c=int(sys.argv[1])+int(sys.argv[2])
	print("sum of that agr", c)

if __name__ =='__main__':
	main()
