a=float(input("enter 1 no."))
b=float(input("enter 2 no."))
c=float(input("enter 3 no."))


def grater():
	if (a>b and a>c):
		print("A is grater")
	if (b>a and b>c):
		print("B is grater")
	if (c>a and c>b):
		print("C is grater")

def smaller():
	if (a<b and a<c):
		print("A is smaller")
	if (b<a and b<c):
		print("B is smaller")
	if (c<a and c<b):
		print("C is smaller")

def equal():
	if (a==b==c):
		print("A,B,C are equal")

def two_are_equal():
	if(a==b and a>c):
		print("A and B both are same and grater and C is smaller")
	else:
		print("A and B both are same and grater and C is grater")
	elif(a==c and a>b):
                print("A and C both are same and grater and B is smaller")
	else:
		print("A and B both are same and grater and C is grater")
	elif(c==b and b>c):
                print("C and B both are same and grater and b is smaller")
	else:
		print("A and B both are same and grater and C is grater")
def main():
	grater()
	smaller()
	equal()
	two_are_equal()
if __name__ == "__main__":
	main()
