arr=[]
n=int(input("enter length of array"))
for i in range (0,n):
    p=input(f"input no. {i+1} ")
    arr.append(int(p))


print(f"your array is {arr}")
som= ullumax(arr)
print(f"Max of your array is {som}")