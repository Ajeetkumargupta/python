#/usr/bin/python
import sys
def without_arg():
	print("Function without Arg")
def with_arg1(fun):
	print("this",fun, "with one arg")
def with_arg2(one,two):
	print("I am",one,"Gupta.""I am previus",two,"of rmlau")
	print("I am",two)

def ajeet():
	without_arg()
	with_arg1(sys.argv[1])
	with_arg2(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
	ajeet()
