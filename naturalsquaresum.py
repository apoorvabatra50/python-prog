def sqrtsum(n):
    sum=0
    for i in range(1,n+1):
        sum= sum+(i*i)
    return sum



y=int(input("enter range for square ssum"))
print(sqrtsum(y))