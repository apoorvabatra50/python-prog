no=int(input("type a no. to check weather it is prime or not and enter: "))
for val in range(2,no-1):
    if no % val == 0:
        print("not a prime no.")
else:
    if no%val !=0:
        print("the no. entered is prime no.")
