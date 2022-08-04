import sys
def add(one,two):
	print("Enter 1 no",one)
	print("Enter 2 no",two)
	c=float(one)+float(two)
	print("Addition of two no.",c)

def sub(one,two):
        print("Enter 1 no",one)
        print("Enter 2 no",two)
        c=float(one)-float(two)
        print("subtraction of two no.",c)

def mul(one,two):
        print("Enter 1 no",one)
        print("Enter 2 no",two)
        c=float(one)*float(two)
        print("multiplication of two no.",c)

def div(one,two):
	print("Enter 1 no",one)
	print("Enter 2 no",two)
	one = float(one)
	two = float(two)
	if two != 0:
		print("division of two no.",one/two)
	else:
		print("Divide by zero is not possible")
def main():
	add(sys.argv[1],sys.argv[2])
	sub(sys.argv[1],sys.argv[2])
	mul(sys.argv[1],sys.argv[2])
	div(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
	main()
