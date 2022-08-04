def main():
#	days=('monday','tuesday','wednesday')
#	for i in days:
#		print(i)
#		print(type(i))
#	print(type(days))
#========================================


	lower=int(input("Enter lower number:- "))
	upper=int(input("Enter upper number:- "))
#	jump=int(input("Enter jumping number:- "))
	number=int(input("Enter The number:- "))
#	for i in range(lower,upper,jump):
	for i in range(lower,upper):

		if i%number ==0:
			print(i)

if __name__ == "__main__":
	main()
