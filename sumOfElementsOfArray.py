def ullu(tom):
    return sum(tom)


arr=[]
n=int(input("enter length of array"))
for i in range (0,n):
    p=input(f"input no. {i+1} ")
    arr.append(int(p))


print(f"your array is {arr}")
som= ullu(arr)
print(f"Sum of your array is {som}")