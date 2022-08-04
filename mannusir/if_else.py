#!usr/bin/python3
import sys

def ajeet(fun):
	if fun=="0":
		print("Switch To The Flight Mode")
	elif fun=="1":
		print("Switch To The Slientt Mode")
	elif fun=="2":
		print("Switch To The DND Mode")
	elif fun=="3":
		print("Switch To The Regular Mode")
	else:
		print("Unknow Mode exist!!!!!!")
def main():
	a=sys.argv[1]
	ajeet(a)
if __name__=="__main__":
	main()
