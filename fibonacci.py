def fib(n):
    if n<0:
        print("incorrect input")

    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


no=int(input("enter a no."))
print(f"fibonacii of the {no} is {fib(no)}")