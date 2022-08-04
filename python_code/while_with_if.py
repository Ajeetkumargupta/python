def main():
	print(" year varrie beetwen 1995 to 2022")
	year=int(input("Enter A number:- "))
	i=1995
	while i<=2022:
		if i==year:
			print("This is my birth year", year)
			i+=1
			#break
			continue
		print(i)
		i=i+1
if __name__ == "__main__":
	main()
